import uuid
from django.template.loader import render_to_string
from protovis.encoders import encoder
from protovis.objects import ProtovisObjects, JavaScriptFragment

class ProtovisMark(object):
    """
    Protovis mark class.
    """
    pv_obj_id = None
    pv_parent_obj_id = None
    pv_class = None
    pv_template = 'protovis/widgets/mark.html'

    def __init__(self, **kwargs):
        """
        Constructor. It also takes any kwargs passed to it
        and sets its key/value pairs as class properties.
        """
        self.__fragments = []
        self.__marks = []
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

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
        return render_to_string(self.pv_template, {'w': self})

    def fragment_closure(self, name):
        """
        Closure function to handle calls to __getattr__
        and recursively build marks and fragments.
        """
        class MarkWrapper(ProtovisMark):
            def __getattr__(self, name):
                new_name = '%s.%s' % (self.pre, name)
                return self.mark.fragment_closure(new_name)

        # handle special cases
        if name in ['label', 'layer', 'link', 'node', '_parent']:
            if name in ['_parent']:
                name = name[1:]
            return MarkWrapper(mark = self, pre = name)

        def handler(*args):

            # if name ends with add, then we are about
            # to switch to another mark
            if name.endswith('add'):

                # generate new object ID
                pv_obj_id = '%s_%s' % (
                    args[0].src.replace('.', ''),
                    str(uuid.uuid4()).replace('-', '')
                )

                # create new mark widget
                m = ProtovisMark(
                    pv_class = args[0],
                    pv_obj_id = pv_obj_id,
                    pv_parent_obj_id = self.pv_obj_id,
                    pv_add_method = name
                )

                # add it to the list of marks
                self.__marks.append(m)
                return m

            # encode JavaScript source
            src = '.%s(%s)' % (name, encoder.encode(args)[1:-1])

            # special case for anchor
            if name.endswith('anchor'):
                return MarkWrapper(mark = self, pre = src[1:])

            # add fragment if not already in fragment list             
            f = JavaScriptFragment(src = src)
            if f not in self.__fragments:
                self.__fragments.append(f)

            return self

        return handler

    def __getattr__(self, name):
        """
        Attach fragment closure function to __getattr__.
        """
        if name.startswith('pv_'):
            # if attribute name begins with 'pv_', then just
            # return the attribute as usual and don't pass it
            # to the fragment closure function
            return object.__getattribute__(self, name)
        else:
            return self.fragment_closure(name)


class ProtovisPanelWidget(ProtovisMark):
    """
    Protovis panel widget.
    """
    pv_obj_id = 'vis'
    pv_parent_obj_id = None
    pv_class = ProtovisObjects().Panel
    pv_template = 'protovis/widgets/widget.html'

    # widget data, width and height
    pv_data = []
    pv_width = 0
    pv_height = 0

    # JavaScript fragment used for initializing stuff
    pv_init_js = JavaScriptFragment(src = '')

    def __unicode__(self):
        """
        Make widgets friendly to Django templates.
        """
        return self.render()
