from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .models import Datapoint, Entity, Label

class AddDatapointView(View):
    def get(self, request):
        entity_types = Entity.objects.all()
        return render(request, 'lab/add_datapoint.html', { 'entity_types': entity_types })

    def post(self, request, *args, **kwargs):
        desc = request.POST['desc']
        d = request.POST['data']
        et_id = request.POST['entity_type']
        et = Entity.objects.get(pk=et_id)
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
        return render(request, 'lab/home.html', {'datapoints': datapoints, 'msg_ok': 'datapoint_added' })
