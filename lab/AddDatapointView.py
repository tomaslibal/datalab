from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from PIL import Image
from io import BytesIO

import tempfile

from .models import Datapoint, Entity, Label

def get_pixels(path, width=32, height=32):
    img = Image.open(path)
    img.thumbnail((width, height), Image.ANTIALIAS)
    p = list(img.getdata())
    #pixels_str = ','.join(str(px[0]) + ',' + str(px[1]) + ',' + str(px[2]) for px in p)
    pixels_str = ','.join(str(px[0]) for px in p)
    return pixels_str, width, height

def handle_uploaded_file(f):
    tmp = tempfile.NamedTemporaryFile(mode='wb+', dir='.')
    for chunk in f.chunks():
        tmp.write(chunk)
    tmp.seek(0)
    #stream = BytesIO(f)
    res = get_pixels(tmp.name)
    tmp.close()
    return res


class AddDatapointView(View):
    def get(self, request):
        entity_types = Entity.objects.all()
        return render(request, 'lab/add_datapoint.html', { 'entity_types': entity_types })

    def post(self, request, *args, **kwargs):
        desc = request.POST['desc']
        d = request.POST['data']
        et_id = request.POST['entity_type']
        et = Entity.objects.get(pk=et_id)
        uploads = request.FILES.get('image', None)
        
        if uploads is not None:
            d, _, _ = handle_uploaded_file(uploads)

        label_names = request.POST.get('labels', [])
        labels = []
        for label in label_names:
            obj, created = Label.objects.get_or_create(
                name=label
            )
            labels.append(obj)

        dp = Datapoint(entity_type=et, data=d, description=desc)
        dp.save()
        dp.labels.add(*labels)
        datapoints = Datapoint.objects.all()
        return HttpResponseRedirect('/', { 'msg_ok': 'datapoint_added' })
        # return render(request, 'lab/home.html', {'datapoints': datapoints, 'msg_ok': 'datapoint_added' })
