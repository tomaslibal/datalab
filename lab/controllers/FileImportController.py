from django.views.generic import View
from django.http import HttpResponse

from lab.controllers.AddDatapointController import handle_uploaded_file

class FileImportController(View):
    def post(self, request):
        et_id = request.POST.get('entity_id', None)

        file = request.FILES.get('file', None)
        label_names = request.POST.getlist('labels[]', [])
        d = handle_uploaded_file(file, et_id, label_names)

        return HttpResponse('OK')
