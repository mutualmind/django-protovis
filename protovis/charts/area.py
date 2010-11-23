from django.utils import simplejson
from protovis.charts.base import ProtovisChart, ValidationError
from protovis.core.objects import js, ProtovisObjects as pv

class AreaChart(ProtovisChart):
    """
    A simple area chart.
    
    Data format:
    [
        { 'x': <x-axis value>, 'y': <y-axis value> },
        { 'x': <x-axis value>, 'y': <y-axis value> },
    ]
    """

    # base properties
    pv_fill_color = '#79ADD2'
    pv_line_width = 3
    pv_stroke_color = '#50748D'
    pv_labels = []
    pv_values = []
    
    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super(AreaChart, self).__init__(*args, **kwargs)
        self.pv_valid_scales_x = [
            pv.Scale.linear,
            pv.Scale.ordinal,
        ]
        self.pv_valid_scales_y = [
            pv.Scale.linear,
            pv.Scale.log,
        ]

    #
    # chart styling
    #    
    def area_fill_color(self, color):
        """
        Set area fill color.
        """
        self.pv_fill_color = color
        return self

    def line_stroke_color(self, color):
        """
        Set line stroke color.
        """
        self.pv_stroke_color = color
        return self
        
    def line_width(self, width):
        """
        Set line width.
        """
        self.pv_line_width = width
        return self

    #
    # chart data and layout
    #
    def parse_data(self):
        """
        Parse data for chart.
        """
        try:
            self.pv_labels = [ x[ 'x' ] for x in self.pv_data ]
            self.pv_values = [ x[ 'y' ] for x in self.pv_data ]
        except:
            raise ValidationError('Could not parse data. Invalid format?')
        return self

    def sizing_and_scales(self):
        self.validate_scales()

        if not len(self.pv_labels):
            raise ValidationError('Missing data labels.')
        
        if not len(self.pv_values):
            raise ValidationError('Missing data values.')
        
        if self.pv_scale_x == pv.Scale.linear:
            max_label = max( self.pv_labels )
            x_scale_js = """
                var x = pv.Scale.linear(0, %(max_label)f).range(0, %(width)i);
            """ % {
                'max_label': max_label,
                'width': self.pv_width,
            }
        else:
            x_scale_js = """
                var categories = data.map(function(d) [d.x]);
                var x = pv.Scale.ordinal(categories).split(0, %(width)i);
            """ % {
                'height': self.pv_height,
                'width': self.pv_width,
            }
        
        max_value = round( max( self.pv_values ) * 1.15 )
        if self.pv_scale_y == pv.Scale.linear:
            y_scale_js = """
                var y = pv.Scale.linear(0, %(max_value)f).range(0, %(height)i);
            """ % {
                'max_value': max_value,
                'height': self.pv_height,
            }
        else:
            min_value = round( min( self.pv_values ) ) 
            y_scale_js = """
                var y = pv.Scale.log(%(min_value)f, %(max_value)f).range(0, %(height)i);
            """ % {
                'max_value': max_value,
                'min_value': min_value,
                'height': self.pv_height,
            }
        
        self.pv_init_js = js(
            """
            var data = %(data)s;
            %(x_scale_js)s
            %(y_scale_js)s
            """ % {
                'data': simplejson.dumps(self.pv_data),
                'x_scale_js': x_scale_js,
                'y_scale_js': y_scale_js,
            }
        )

    def y_axis(self):
        self.add(pv.Rule) \
            .data(js('y.ticks()')) \
            .visible(js('function(d) d'))\
            .bottom(js('y')) \
            .strokeStyle(js('function(d) d ? "#EEE" : "#000"')) \
            .anchor('left').add(pv.Label) \
                .text(js('y.tickFormat'))

    def x_axis(self):
        if self.pv_scale_x == pv.Scale.linear:
            self.add(pv.Rule) \
                .data(js('x.ticks()')) \
                .visible(js('function(d) d'))\
                .left(js('x')) \
                .bottom(-5) \
                .height(5) \
                .anchor('bottom').add(pv.Label) \
                    .text(js('x.tickFormat'))
        elif self.pv_scale_x == pv.Scale.ordinal:
            self.add(pv.Rule) \
                .data(js('categories')) \
                .left(js('x')) \
                .bottom(-5) \
                .height(5) \
                .anchor('bottom').add(pv.Label)

    def area_line(self):
        self.add(pv.Area) \
            .data(js('data')) \
            .bottom(1) \
            .left(js('function(d) x(d.x)')) \
            .height(js('function(d) y(d.y)')) \
            .fillStyle(self.pv_fill_color) \
            .anchor('top').add(pv.Line) \
                .strokeStyle(self.pv_stroke_color) \
                .lineWidth(self.pv_line_width)

    def finalize(self):
        """
        Finalize layout.
        """
        super(AreaChart, self).finalize()
        self.y_axis()
        self.x_axis()
        self.area_line()
