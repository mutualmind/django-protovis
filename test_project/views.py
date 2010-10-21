from django.http import HttpResponse
from protovis.charts.demo import DemoChartWidget

def gallery(request):
    chart = DemoChartWidget()
    return HttpResponse(chart.render())
