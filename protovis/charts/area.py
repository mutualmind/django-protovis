from protovis.charts.base import BaseChartWidget
from protovis.objects import js


class AreaChartWidget(BaseChartWidget):
    """A simple area chart"""
    
    def __init__(self, *args, **kwargs):
        super(AreaChartWidget, self).__init__(*args, **kwargs)
        self.y_axis()
        self.x_axis()
        self.top_line()

    def sizing_and_scales(self):
        self.pv_init_js = js(
            """
            var data = %(data)s;
            var x = pv.Scale.linear(data, function(d) d.x).range(0, %(w)i);
            var y = pv.Scale.linear(0, 4).range(0, %(h)i);
            """ % {
                'data': self.pv_data,
                'w': self.pv_width,
                'h': self.pv_height,
            }
        )

    def y_axis(self):
        self.add(self.pv.Rule) \
            .data(js('y.ticks(5)')) \
            .bottom(js('y')) \
            .strokeStyle(js('function(d) d ? "#EEE" : "#000"')) \
            .anchor('left').add(self.pv.Label) \
                .text(js('y.tickFormat'))

    def x_axis(self):
        self.add(self.pv.Rule) \
            .data(js('x.ticks()')) \
            .visible(js('function(d) d')) \
            .left(js('x')) \
            .bottom(-5) \
            .height(5) \
            .anchor('bottom').add(self.pv.Label) \
                .text(js('x.tickFormat'))

    def top_line(self):
        self.add(self.pv.Area) \
            .data(js('data')) \
            .bottom(1) \
            .left(js('function(d) x(d.x)')) \
            .height(js('function(d) y(d.y)')) \
            .fillStyle('rgb(121,173,210)') \
            .anchor('top').add(self.pv.Line) \
                .lineWidth(3)
