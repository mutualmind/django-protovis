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
        self.pv_data = js("""pv.range(0, 10, .1).map(function(x) {
                return {x: x, y: Math.sin(x) + Math.random() * .5 + 2};
            })""").src

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
            .strokeStyle(js('function(d) d ? pv.Color.Rgb(200,200,200) : pv.Color.Rgb(0,0,0)')) \
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
            .fillStyle(js('pv.Color.Rgb(121,173,210)')) \
            .anchor('top').add(pv.Line) \
            .lineWidth(3)
