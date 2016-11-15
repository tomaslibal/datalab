from django.shortcuts import render
from django.http import HttpResponse

from PIL import Image

from math import sqrt

from .models import Datapoint, Entity

# Create your views here.
def home(request):
    datapoints = Datapoint.objects.all()
    return render(request, 'lab/home.html', {'datapoints': datapoints})

def edit_labels(request, datapoint_id):
    datapoint = Datapoint.objects.filter(id=datapoint_id)
    return render(request, 'lab/edit_labels.html', {'datapoint': datapoint})

def add_datapoint(request):
    entity_types = Entity.objects.all()
    return render(request, 'lab/add_datapoint.html', { 'entity_types': entity_types })

def entity_image(request, datapoint_id, out_w=32, out_h=32):
    # passed in arguments from django url are always strings
    out_w = int(out_w)
    out_h = int(out_h)
    datapoint = Datapoint.objects.get(pk=datapoint_id)
    pixels = datapoint.data.split(',')
    num_pixels = len(pixels)
    w = int(sqrt(num_pixels))

    response = HttpResponse(content_type="image/png")
    img = Image.new('RGB', (w, w))
    
    rgb = []
    for px in pixels:
        rgb.append((int(px), 0, 0))

    img.putdata(rgb)
    img.thumbnail((out_w, out_h), Image.ANTIALIAS)
    img.save(response, "PNG")
    return response

