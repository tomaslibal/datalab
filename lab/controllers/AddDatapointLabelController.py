from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from lab.models import Datapoint, Label

class AddDatapointLabelController(View):
    def get(self, request):
        return HttpResponseRedirect('/lab/home.html')
    def post(self, request, datapoint_id):
        label_name = request.POST.get('name', None)
        if label_name is not None:
            obj, created = Label.objects.get_or_create(name=label_name)
            dp = Datapoint.objects.get(id=datapoint_id)
            dp.labels.add(obj)
            dp.save()
            return HttpResponse('OK')
        return HttpResponseNotFound('Error: datapoint id not found')
