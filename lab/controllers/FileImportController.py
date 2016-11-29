from django.views.generic import View
from django.http import HttpResponse

from lab.controllers.AddDatapointController import handle_uploaded_file
from lab.models import Datapoint, UserDefinedEntity, Label

class FileImportController(View):
    def post(self, request):
        et_id = request.POST.get('entity_id', None)
        et = UserDefinedEntity.objects.get(pk=et_id)
        file = request.FILES.get('file', None)
        d, _, _ = handle_uploaded_file(file, et.entity_type)
        dp = Datapoint(entity_type=et, name="Imported", data=d, description="")
        dp.save()
        label_names = request.POST.getlist('labels[]', [])
        for label in label_names:
            if len(label) > 0:
                obj, created = Label.objects.get_or_create(
                    name=label
                )
                dp.labels.add(obj)

        dp.save()
        return HttpResponse('OK')
