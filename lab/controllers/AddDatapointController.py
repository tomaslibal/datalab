from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.apps import apps

from PIL import Image
from io import BytesIO

import tempfile


from lab.models import Datapoint, UserDefinedEntity, Label

def get_pixels(path, width=96, height=96):
    img = Image.open(path)
    img = img.resize((width, height), resample=Image.BILINEAR)
    p = list(img.getdata())
    #pixels_str = ','.join(str(px[0]) + ',' + str(px[1]) + ',' + str(px[2]) for px in p)
    pixels_str = ','.join(str(px[0]) for px in p)
    return pixels_str, width, height

def handle_uploaded_file(f):
    tmp = tempfile.NamedTemporaryFile(mode='wb+', dir='.')
    for chunk in f.chunks():
        tmp.write(chunk)
    tmp.seek(0)
    res = get_pixels(tmp.name)
    tmp.close()
    return res


class AddDatapointController(View):
    def get(self, request):
        entity_types = UserDefinedEntity.objects.all()
        return render(request, 'lab/add_datapoint.html', { 'entity_types': entity_types })

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        desc = request.POST['desc']
        d = request.POST['data']
        et_id = request.POST['entity_type']
        et = UserDefinedEntity.objects.get(pk=et_id)
        uploads = request.FILES.get('image', None)
        
        if uploads is not None:
            d, _, _ = handle_uploaded_file(uploads)

        label_names = request.POST.getlist('labels[]', [])

        dp = Datapoint(entity_type=et, name=name, data=d, description=desc)
        dp.save()        

        for label in label_names:
            if len(label) > 0:
                obj, created = Label.objects.get_or_create(
                    name=label
                )
                dp.labels.add(obj)

        dp.save()
        return HttpResponseRedirect('/', { 'msg_ok': 'datapoint_added' })
