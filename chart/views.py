# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def barchart(request):

    # instantiate a drawing object
    from . import my_charts
    d = my_charts.MyBarChartDrawing()

    # extract the request params of interest.
    # I suggest having a default for everything.
    if 'height' in request:
        d.height = int(request['height'])
    if 'width' in request:
        d.width = int(request['width'])
    
    if 'numbers' in request:
        strNumbers = request['numbers']
        numbers = map(int, strNumbers.split(','))
        d.chart.data = [numbers]   # bar charts take a list-of-lists for data

    if 'title' in request:
        d.title.text = request['title']
  
    # get a GIF (or PNG, JPG, or whatever)
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')
