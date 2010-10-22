from protovis.charts.base import BaseChartWidget
from protovis.objects import js


class BarChartWidget(BaseChartWidget):
    
    def __init__(self, *args, **kwargs):
        super(BarChartWidget, self).__init__(*args, **kwargs)
        self.bars()
        self.value_label()
        self.variable_label()
        self.x_axis()
    
    def sizing_and_scales(self):
        self.pv_init_js = js(
            """
            var data = %(data)s;
            var x = pv.Scale.linear(0, 1.1).range(0, %(w)i)
            var y = pv.Scale.ordinal(pv.range(10)).splitBanded(0, %(h)i, 4/5);
            """ % {
                'data': self.pv_data,
                'w': self.pv_width,
                'h': self.pv_heght,
            }
        )
    
    def bars(self):
        self.pv_bar = self.add(self.pv.Bar) \
            .data(self.pv_data) \
            .top(js('function() y(this.index)')) \
            .height(js('y.range().band')) \
            .left(0) \
            .width(js('x'))
    
    def value_label(self):
        self.pv_bar.anchor('right').add(self.pv.Label) \
            .textStyle('white') \
            .text(js'function(d) d.toFixed(1)')
    
    def variable_label(self):
        self.pv_bar.anchor('left') \
            .textMargin(5) \
            .textAlign('right') \
            .text(js'function() "ABCDEFGHIJK".charAt(this.index)')
    
    def x_axis(self):
        self.add(self.pv.Rule) \
            .data(js('x.ticks(5)')) \
            .left(js('x')) \
            .strokeStyle(
                js('function(d) d ? "rgba(255,255,255,.3)" : "#000"')
            ) \
          .add(self.pv.Rule) \
            .bottom(0) \
            .height(5) \
            .strokeStyle("#000") \
          .anchor("bottom").add(self.pv.Label)
            .text(js('x.tickFormat'));
