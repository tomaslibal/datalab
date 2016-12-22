from django.views.generic import View
from django.http import HttpResponseRedirect

from lab.models import UserDefinedEntity

class AddEntityController(View):
    def post(self, request):
        name = request.POST['name']
        desc = request.POST['desc']
        entity_type = request.POST['entity_type']

        e = UserDefinedEntity(name=name, description=desc, entity_type=entity_type)
        e.save()

        return HttpResponseRedirect('/entities', {'msg_ok': 'datapoint_added'})