from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.apps import apps

from PIL import Image

from math import sqrt

from .models import Datapoint, UserDefinedEntity, Label, Dataset
from .util.ImageHash import ImageHash

def getObjectsPaginator(collection, page_by, request):
    paginator = Paginator(collection, page_by)
    page = request.GET.get('page', 1)
    try:
        collection = paginator.page(page)
    except PageNotAnInteger:
        collection = paginator.page(1)
    except EmptyPage:
        collection = paginator.page(paginator.num_pages)
    return collection

def getHashVal(datapoint):
    if datapoint.entity_type is 'img':
        h = ImageHash()

        pixels = datapoint.data.split(',')
        num_pixels = len(pixels)
        w = int(sqrt(num_pixels))

        pixels_r = [[pixels[i * j] for i in range(w)] for j in range(w)]

        return h.hash(pixels_r)
    else:
        return 'n/a'




def home(request):
    latest_dps = Datapoint.objects.order_by('-id')[:16]
    return render(request, 'lab/home.html', { 'latest_dps': latest_dps })

def datapoints(request):
    page_by = apps.get_app_config('lab').paginate_by
    datapoints = Datapoint.objects.all()
    datapoints = getObjectsPaginator(datapoints, page_by, request)

    return render(request, 'lab/datapoints.html', {'datapoints': datapoints})

def datapoint_details(request, datapoint_id):
    entity_types = UserDefinedEntity.objects.all()
    datapoint = Datapoint.objects.get(id=datapoint_id)

    hashval = getHashVal(datapoint)

    sets = Dataset.objects.all()

    return render(request, 'lab/detail_datapoint.html', { 'datapoint': datapoint, 'entity_types': entity_types, 'hashval': hashval, 'datasets': sets })

def delete_dp_label(request, datapoint_id, label_id):
    label = Label.objects.get(id=label_id)
    Datapoint.objects.get(id=datapoint_id).labels.remove(label)
    return HttpResponse('OK')

def datasets(request):
    sets = Dataset.objects.all()
    return render(request, 'lab/datasets.html', { 'datasets': sets })

@csrf_protect
def imports(request):
    entity_types = UserDefinedEntity.objects.all()
    return render(request, 'lab/import.html', { 'entity_types': entity_types })

def settings(request):
    settings = {}
    return render(request, 'lab/settings.html', { 'settings': settings })

def edit_labels(request, datapoint_id):
    datapoint = Datapoint.objects.filter(id=datapoint_id)
    return render(request, 'lab/edit_labels.html', {'datapoint': datapoint})

def add_datapoint(request):
    entity_types = UserDefinedEntity.objects.all()
    return render(request, 'lab/add_datapoint.html', { 'entity_types': entity_types })

def entities(request):
    entities = UserDefinedEntity.objects.all()
    return render(request, 'lab/entities.html', { 'entities': entities })

def entity_detail(request, entity_id):
    entity = UserDefinedEntity.objects.get(id=entity_id)
    return render(request, 'lab/detail_entity.html', { 'entity': entity })

def labels(request):
    labels = Label.objects.all()
    page_by = apps.get_app_config('lab').paginate_by
    labels = getObjectsPaginator(labels, page_by, request)
    return render(request, 'lab/labels.html', { 'labels': labels })

def label_details(request, label_id):
    label = Label.objects.get(id=label_id)
    return render(request, 'lab/detail_label.html', { 'label': label })

def label_delete(request, label_id):
    Label.objects.filter(id=label_id).delete()
    return HttpResponse('OK', content_type="text/plain")

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

