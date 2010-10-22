import math
import random

from django.shortcuts import render_to_response
from django.template import RequestContext

from protovis.charts.area import AreaChartWidget

def demo(request):
    data = [
        {'x': x / 10.0, 'y': math.sin(x / 10) + random.random() * 0.5 + 2}
        for x in range(0, 100)
    ]
    
    chart = AreaChartWidget(width=400, height=200, data=data)

    template = 'examples.html'
    data = {
        'chart': chart,
    }

    return render_to_response(template, data,
                               context_instance = RequestContext(request))
