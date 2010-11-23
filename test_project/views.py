import math
import random

from django.shortcuts import render_to_response
from django.template import RequestContext

from protovis.charts.area import AreaChart
from protovis.core.objects import ProtovisObjects as pv

def demo(request):
    data = [
        {'x': x / 10.0, 'y': math.sin(x / 10) + random.random() * 0.5 + 2}
        for x in range(0, 100)
    ]
    
    chart = AreaChart(
        width = 400, height = 200, data = data
    ).scale_x(
        pv.Scale.linear
    ).scale_y(
        pv.Scale.log
    ).area_fill_color(
        '#E3EEF8'
    ).line_stroke_color(
        '#2365BD'
    )

    template = 'examples.html'
    data = {
        'chart': chart,
    }

    return render_to_response(template, data,
                              context_instance = RequestContext(request))
