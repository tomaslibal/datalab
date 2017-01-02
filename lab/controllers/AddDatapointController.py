from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View

import tempfile

from lab.lib.GenericEntityProcessor import GenericEntityProcessor
from lab.lib.ImageEntityProcessor import ImageEntityProcessor
from lab.models import Datapoint, UserDefinedEntity, Label


def handle_uploaded_file(f, entity_id, labels):
    et = UserDefinedEntity.objects.get(pk=entity_id)
    tmp = tempfile.NamedTemporaryFile(mode='wb+', dir='.')
    for chunk in f.chunks():
        tmp.write(chunk)
    tmp.seek(0)
    if et.entity_type is 'img':
        res = ImageEntityProcessor.process(tmp.name, labels, et)
    else:
        print("****************" + entity_id)
        res = GenericEntityProcessor.process(tmp.name, labels, et)
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
        uploads = request.FILES.get('image', None)
        label_names = request.POST.getlist('labels[]', [])
        
        if uploads is not None:
            dp = handle_uploaded_file(uploads, et_id, label_names)
        else:
            et_type = UserDefinedEntity.objects.get(pk=et_id)
            dp = Datapoint(name=name, description=desc, data=d, entity_type=et_type)
            dp.save()
            # add labels...

        dp.name = name
        dp.description = desc
        dp.save()

        return HttpResponseRedirect('/?msg_ok=datapoint_added')
