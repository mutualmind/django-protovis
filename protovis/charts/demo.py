import random
from protovis.objects import ProtovisObjects, js
from protovis.widgets import ProtovisPanelWidget

class DemoChartWidget(ProtovisPanelWidget):
    width = 640
    height = 480
    
    def __init__(self, *args, **kwargs):
        self.data = [
            [ random.random() + 0.1 for j in range(4) ] for i in range(3)
        ]
        super(DemoChartWidget, self).__init__(*args, **kwargs)
        
        # Protovis objects
        pv = ProtovisObjects()

        # sizing and scales
        self.init_js = js(
            """
            var data = %s;
            var n = data.length;
            var m = data[0].length;
            var w = %i,
                h = %i,
                x = pv.Scale.linear(0, 1.1).range(0, w),
                y = pv.Scale.ordinal(pv.range(n)).splitBanded(0, h, 4/5);
            """ % (self.data, self.width, self.height)
        )

        # init self after setting all the properties
        self.init()

        # the bars
        bar = self.add(pv.Panel) \
            .data(js('data')) \
            .top(js('function() y(this.index)')) \
            .height(js('y.range().band')) \
            .add(pv.Bar) \
            .data(js('function(d) d')) \
            .top(js('function() this.index * y.range().band / m')) \
            .height(js('y.range().band / m')) \
            .left(0) \
            .width(js('x')) \
            .fillStyle(js('pv.Colors.category20().by(pv.index)'))

        # the value label
        bar.add(pv.Label) \
            .textStyle('white') \
            .text(js('function(d) d.toFixed(1)')) \
            .anchor('right')

        # The variable label
        bar.add(pv.Label) \
            .textAlign('right') \
            .textMargin(5) \
            .text(js('function() "ABCDEFGHIJK".charAt(this.parent.index)')) \
            .anchor('left')

        # X-axis ticks.
        self.add(pv.Rule) \
            .data(js('x.ticks(5)')) \
            .left(js('x')) \
            .strokeStyle(js('function(d) d ? "rgba(255,255,255,.3)" : "#000"'))\
            .add(pv.Rule) \
            .bottom(0) \
            .height(5) \
            .strokeStyle('#000') \
            .anchor('bottom')
