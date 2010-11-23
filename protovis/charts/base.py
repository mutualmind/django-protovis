from protovis.core.widgets import ProtovisPanel


class ValidationError( Exception ):
    """
    Thrown when any phase of a chart's layout fails validation.
    """
    pass


class ProtovisChart(ProtovisPanel):
    """
    A base chart widget defining common elements that apply to most
    conventional charts.
    """
    # base properties
    pv_bottom = 20
    pv_top = 5
    pv_left = 20
    pv_right = 10
    
    # valid scales for chart and selected scales
    # sub-classes have to set these to whatever is valid for each chart
    # type
    pv_valid_scales_x = []
    pv_valid_scales_y = []
    pv_scale_x = None
    pv_scale_y = None

    def __init__(self, width, height, data, *args, **kwargs):
        """
        Constructor.
        """
        self.pv_width = width
        self.pv_height = height
        self.pv_data = data
        super(ProtovisChart, self).__init__(*args, **kwargs)

    #
    # chart styling
    #    
    def padding_top(self, padding):
        """
        Set top padding for root panel.
        """
        self.pv_top = padding
        return self
        
    def padding_bottom(self, padding):
        """
        Set bottom padding for root panel.
        """
        self.pv_bottom = padding
        return self
        
    def padding_left(self, padding):
        """
        Set left padding for root panel.
        """
        self.pv_left = padding
        return self
        
    def padding_right(self, padding):
        """
        Set right padding for root panel.
        """
        self.pv_right = padding
        return self

    def scale_x(self, scale):
        """
        Set scale for the x-axis.
        """
        if len(self.pv_valid_scales_x) and scale not in self.pv_valid_scales_x:
            raise ValidationError('Selected x-axis scale is not supported.')
        self.pv_scale_x = scale
        return self
        
    def scale_y(self, scale):
        """
        Set scale for the y-axis.
        """
        if len(self.pv_valid_scales_y) and scale not in self.pv_valid_scales_y:
            raise ValidationError('Selected y-axis scale is not supported.')
        self.pv_scale_y = scale
        return self

    #
    # chart data and layout
    # these should never be called directly
    #
    def parse_data(self):
        """
        This abstract method needs to implement the code
        needed to parse the data passed in via the constructor.
        """
        raise NotImplementedError('parse_data method not implemented.')
    
    def validate_scales(self):
        if self.pv_scale_x is None:
            raise ValidationError('Scale for x-axis has not been set.')
        if self.pv_scale_y is None:
            raise ValidationError('Scale for y-axis has not been set.')
    
    def sizing_and_scales(self):
        """
        This abstract method needs to implement the code
        needed to set up the basic chart components including
        data structures, x-axis, y-axis and scales.
        """
        raise NotImplementedError('sizing_and_scales method not implemented.')

    def root_panel(self):
        """
        Set up the root panel.
        """
        self.width(self.pv_width) \
            .height(self.pv_height) \
            .top(self.pv_top) \
            .bottom(self.pv_bottom) \
            .left(self.pv_left) \
            .right(self.pv_right)

    def finalize(self):
        """
        Finalize the chart layout. Should be called at the
        very end after all requirued chart styling and layout methods
        are called.

        Sub-classes may add their own custom layout methods
        to the layout call chain after calling super.finalize().
        
        May throw a ValidationError if something goes wrong
        at any step.
        """
        self.parse_data()
        self.root_panel()
        self.sizing_and_scales()

    def render(self):
        """
        Render the chart for display using the Django
        template system.
        """
        self.finalize()
        return super(ProtovisChart, self).render()
    
    def __unicode__(self):
        """
        Make widgets friendly to Django templates.
        """
        return self.render()
