import re
from django.core.serializers.json import DjangoJSONEncoder
from protovis.objects import JavaScriptFragment

class ProtovisEncoder(DjangoJSONEncoder):
    def __init__(self, *args, **kwargs):
        super(ProtovisEncoder, self).__init__(*args, **kwargs)

    def default(self, obj):
        if isinstance(obj, JavaScriptFragment):
            return self.mark_for_escape(obj)
        return super(ProtovisEncoder, self).default(obj)

    def encode(self, obj):
        self.unescape_symbols = {}
        encoded = super(ProtovisEncoder, self).encode(obj)
        unescaped = self.unescape_marked(encoded)
        self.unescape_symbols = {}
        return unescaped

    def mark_for_escape(self, obj):
        self.unescape_symbols[id(obj)] = obj
        return 'ProtovisEncoder_unescape_' + str(id(obj))

    def unescape_marked(self, encoded):
        unescape_pattern = re.compile('"ProtovisEncoder_unescape_([0-9]*)"')
        def unescape(match):
            try:
                obj_id = int(match.group(1))
                obj = self.unescape_symbols[obj_id]
                return obj.src
            except:
                # simply return the match if there is a problem
                return match.group(0)
        return unescape_pattern.sub(unescape, encoded)

protovis_encoder = ProtovisEncoder()