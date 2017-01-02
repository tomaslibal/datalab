from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.apps import apps

from PIL import Image

from math import sqrt

from .lib.AvailableEntities import AVAILABLE_ENTITIES
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

def datasets(request):
    sets = Dataset.objects.all()
    if len(sets) is 0:
        sets = None
    return render(request, 'lab/datasets.html', { 'datasets': sets })

@csrf_protect
def imports(request):
    entity_types = UserDefinedEntity.objects.all()
    datasets = Dataset.objects.all()
    return render(request, 'lab/import.html', { 'entity_types': entity_types, 'datasets': datasets })

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

def add_entity(request):
    entities = []
    for tuple in AVAILABLE_ENTITIES:
        entities.append({ 'id': tuple[0], 'name': tuple[1]})
    return render(request, 'lab/add_entity.html', { 'avail_entities': entities })


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

