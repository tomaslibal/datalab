from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from PIL import Image

from math import sqrt

from .models import Datapoint, Entity, Label

def home(request):
    latest_dps = Datapoint.objects.order_by('-id')[:16]
    return render(request, 'lab/home.html', { 'latest_dps': latest_dps })

def datapoints(request):
    datapoints = Datapoint.objects.all()
    return render(request, 'lab/datapoints.html', {'datapoints': datapoints})

def datapoint_details(request, datapoint_id):
    entity_types = Entity.objects.all()
    datapoint = Datapoint.objects.get(id=datapoint_id)
    return render(request, 'lab/detail_datapoint.html', { 'datapoint': datapoint, 'entity_types': entity_types })

def delete_dp_label(request, datapoint_id, label_id):
    label = Label.objects.get(id=label_id)
    Datapoint.objects.get(id=datapoint_id).labels.remove(label)
    return HttpResponse('OK')

def datasets(request):
    return render(request, 'lab/datasets.html', {})

@csrf_protect
def imports(request):
    entity_types = Entity.objects.all()
    return render(request, 'lab/import.html', { 'entity_types': entity_types })

def settings(request):
    settings = {}
    return render(request, 'lab/settings.html', { 'settings': settings })

def edit_labels(request, datapoint_id):
    datapoint = Datapoint.objects.filter(id=datapoint_id)
    return render(request, 'lab/edit_labels.html', {'datapoint': datapoint})

def add_datapoint(request):
    entity_types = Entity.objects.all()
    return render(request, 'lab/add_datapoint.html', { 'entity_types': entity_types })

def entities(request):
    entities = Entity.objects.all()
    return render(request, 'lab/entities.html', { 'entities': entities })

def entity_detail(request, entity_id):
    entity = Entity.objects.get(id=entity_id)
    return render(request, 'lab/detail_entity.html', { 'entity': entity })

def labels(request):
    labels = Label.objects.all()
    return render(request, 'lab/labels.html', { 'labels': labels })

"""
returns how many datapoints use the given label
"""
def num_datapoints_use_label(request, label_id):
    num = Datapoint.objects.filter(labels__id__exact=label_id).count()
    response = HttpResponse(num, content_type="text/plain")
    return response   

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
        rgb.append((int(px), int(px), int(px)))

    img.putdata(rgb)
    img.thumbnail((out_w, out_h), Image.ANTIALIAS)
    img.save(response, "PNG")
    return response

