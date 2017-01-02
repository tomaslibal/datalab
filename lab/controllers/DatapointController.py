from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View

from lab.models import Datapoint, UserDefinedEntity, Label

import json

class DatapointController(View):
    def get(self, request, datapoint_id):
        dp = Datapoint.objects.get(pk=datapoint_id)
        jsondata = {
            'name': dp.name
        }
        return HttpResponse(json.dumps(jsondata), content_type='application/json')

    def post(self, request, *args, **kwargs):
        dp_id = request.POST['dp_id']
        name = request.POST['name']
        desc = request.POST['desc']
        d = request.POST['data']
        et_id = request.POST['entity_type']
        et_type = UserDefinedEntity.objects.get(pk=et_id)
        uploads = request.FILES.get('datafile', None)

        dp = Datapoint.objects.get(pk=dp_id)
        dp.name = name
        dp.description = desc
        dp.entity_type = et_type
        dp.data = d
        dp.save()
        
        """
        if uploads is not None:
            dp = handle_uploaded_file(uploads, et_id, label_names)
        else:
            dp = Datapoint(name=name, description=desc, data=d, entity_type=et_type)
            dp.save()            
        
        dp.name = name
        dp.description = desc
        dp.save()
        """

        return HttpResponseRedirect('/datapoint/' + dp_id + '?msg_ok=datapoint_updated')
