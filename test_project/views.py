from django.shortcuts import render_to_response
from django.template import RequestContext
from protovis.charts.demo import DemoChartWidget

def demo(request):
    chart = DemoChartWidget()

    template = 'protovis/chart.html'
    data = {
        'chart': chart,
    }

    return render_to_response(template, data,
                               context_instance = RequestContext(request))
