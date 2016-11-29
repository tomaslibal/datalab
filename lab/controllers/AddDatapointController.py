from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

import tempfile

from lab.lib.GenericEntityProcessor import GenericEntityProcessor
from lab.lib.ImageEntityProcessor import ImageEntityProcessor
from lab.models import Datapoint, UserDefinedEntity, Label


def handle_uploaded_file(f, entity_type):
    tmp = tempfile.NamedTemporaryFile(mode='wb+', dir='.')
    for chunk in f.chunks():
        tmp.write(chunk)
    tmp.seek(0)
    if entity_type == 'img':
        res = ImageEntityProcessor.process(tmp.name)
    else:
        res = GenericEntityProcessor.process(tmp.name)
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
            d, _, _ = handle_uploaded_file(uploads, et.entity_type)

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
