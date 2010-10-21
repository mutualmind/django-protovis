import uuid
from django.template.loader import render_to_string
from protovis.encoders import protovis_encoder
from protovis.objects import ProtovisObjects, JavaScriptFragment

class ProtovisMark(object):
    """
    Protovis mark class.
    """
    obj_id = None
    parent_obj_id = None
    protovis_cls = None

    # template to use for rendering self
    template = 'protovis/widgets/mark.html'

    # internal stuff
    __initialized = False
    __fragments = None
    __marks = None

    def __init__(self, **kwargs):
        """
        Constructor which simply takes the kwargs
        and sets the key/value pairs as class properties.
        """
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def init(self):
        """
        Late initializer.
        """
        self.__fragments = []
        self.__marks = []
        self.__initialized = True
        return self

    @classmethod
    def create_instance(cls, **kwargs):
        """
        Generate instance of a mark.
        """
        instance = object.__new__(cls)
        instance.__init__(**kwargs)
        return instance

    def get_fragments(self):
        """
        Return list of JavaScript fragments.
        """
        return self.__fragments

    def get_marks(self):
        """
        Return list of added marks.
        """
        return self.__marks

    def render(self):
        """
        Render self for display in template.
        """
        return render_to_string(self.template, {
            'widget': self,
            'obj_id': object.__getattribute__(self, 'obj_id'),
            'parent_obj_id': object.__getattribute__(self, 'parent_obj_id'),
            'protovis_cls': object.__getattribute__(self, 'protovis_cls'),
        })

    def fragment_closure(self, name):
        """
        Closure function to handle calls to __getattr__
        and recursively build marks and fragments.
        """
        class NameExtensionWrapper(ProtovisMark):
            def __getattr__(self, name):
                return self.mark.fragment_closure('%s.%s' % (self.pre, name))

        # handle special cases
        if name in ['label', 'layer', 'link', 'node', '_parent']:
            if name in ['_parent']:
                name = name[1:]
            return NameExtensionWrapper(mark=self, pre=name).create_instance().init()

        def handler(*args, **kwargs):
            if not self.__initialized:
                raise ValueError, 'Widget not initialized.'
            if kwargs:
                raise ValueError, 'Keyword arguments are not allowed.'

            # if name ends with add, then we are about
            # to switch to another mark
            if name.endswith('add'):

                # generate new object ID
                obj_id = '%s_%s' % (
                    args[0].src.replace('.', ''),
                    str(uuid.uuid4()).replace('-', '')
                )

                # create new mark widget
                m = ProtovisMark(
                    protovis_cls=args[0],
                    obj_id=obj_id,
                    parent_obj_id=self.obj_id
                ).create_instance().init()

                # add it to the list of marks
                self.__marks.append(m)
                return m

            # encode JavaScript source
            src = '.%s(%s)' % (name, protovis_encoder.encode(args)[1:-1])

            # special case for anchor
            if name.endswith('anchor'):
                return NameExtensionWrapper(mark=self, pre=src[1:]).create_instance().init()

            # add fragment if not already in fragment list             
            f = JavaScriptFragment(src=src)
            if f not in self.__fragments:
                self.__fragments.append(f)

            return self

        return handler

    def __getattr__(self, name):
        """
        Attach fragment closure function to __getattr__.
        """
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return self.fragment_closure(name)


class ProtovisPanelWidget(ProtovisMark):
    """
    Protovis panel widget.
    """
    obj_id = 'vis'
    parent_obj_id = None
    protovis_cls = ProtovisObjects().Panel
    template = 'protovis/widgets/widget.html'
    
    # widget data, width and height
    data = []
    width = 0
    height = 0

    # JavaScript fragment used for initializing stuff
    init_js = JavaScriptFragment(src='')
