from django.views.generic import View
from django.http import HttpResponse

from lab.controllers.AddDatapointController import handle_uploaded_file, get_pixels
from lab.models import Datapoint, Entity

class FileImportController(View):
    def post(self, request):
        et_id = request.POST.get('entity_id', None)
        et = Entity.objects.get(pk=et_id)
        file = request.FILES.get('file', None)
        d, _, _ = handle_uploaded_file(file)
        dp = Datapoint(entity_type=et, name="Imported", data=d, description="")
        dp.save()
        return HttpResponse('OK')
