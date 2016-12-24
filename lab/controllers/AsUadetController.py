from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.encoding import smart_str

import tempfile

from lab.models import Datapoint

class AsUadetController(View):
    def get(self, request):
        dataset_ids = request.GET.get('dataset_ids').split(',')

        with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt') as tmp:
            datapoints = Datapoint.objects.filter(dataset__id__in=dataset_ids)
            for dp in datapoints:
                labels = []
                for label in dp.labels.all():
                    labels.append(label.name)
                if len(labels) > 0:
                    first_col = ",".join(labels) + '\t'
                else:
                    first_col = ''
                tmp.write(first_col + str(dp.data) + '\n')
            tmp.seek(0)  
            content = smart_str(tmp.read())  
            res = HttpResponse(content, content_type='application/force-download') 
            res['Content-Disposition'] = 'attachment; filename=%s' % smart_str(tmp.name)
            res['Content-Length'] = len(content)
            return res
        return render(request, 'lab/error_download.html', { 'type': 'uadet' })
