import math
import random
from protovis.objects import ProtovisObjects, js
from protovis.widgets import ProtovisPanelWidget

class DemoChartWidget(ProtovisPanelWidget):
    pv_width = 400
    pv_height = 200

    def __init__(self, *args, **kwargs):
        super(DemoChartWidget, self).__init__(*args, **kwargs)

        # Protovis objects
        pv = ProtovisObjects()

        # data generator
        self.pv_data = [
            {'x': x / 10.0, 'y': math.sin(x / 10) + random.random() * 0.5 + 2}
            for x in range(0, 100)
        ]

        # sizing and scales
        self.pv_init_js = js(
            """
            var data = %(data)s;
            var w = %(width)i;
            var h = %(height)i;
            var x = pv.Scale.linear(data, function(d) d.x).range(0, w);
            var y = pv.Scale.linear(0, 4).range(0, h);            
            """ % {
                'data': self.pv_data,
                'width': self.pv_width,
                'height': self.pv_height,
            }
        )

        # root panel
        self.width(js('w')) \
            .height(js('h')) \
            .bottom(20) \
            .left(20) \
            .right(10) \
            .top(5)

        # y-axis and ticks
        self.add(pv.Rule) \
            .data(js('y.ticks(5)')) \
            .bottom(js('y')) \
            .strokeStyle(js('function(d) d ? "#EEE" : "#000"')) \
            .anchor('left').add(pv.Label) \
                .text(js('y.tickFormat'))

        # x-axis and ticks
        self.add(pv.Rule) \
            .data(js('x.ticks()')) \
            .visible(js('function(d) d')) \
            .left(js('x')) \
            .bottom(-5) \
            .height(5) \
            .anchor('bottom').add(pv.Label) \
                .text(js('x.tickFormat'))

        # the area with top line
        self.add(pv.Area) \
            .data(js('data')) \
            .bottom(1) \
            .left(js('function(d) x(d.x)')) \
            .height(js('function(d) y(d.y)')) \
            .fillStyle('rgb(121,173,210)') \
            .anchor('top').add(pv.Line) \
                .lineWidth(3)
