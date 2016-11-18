from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.encoding import smart_str

import tempfile

from lab.models import Datapoint

class AsCsvController(View):
    def get(self, request):
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv') as tmp:
            datapoints = Datapoint.objects.all()
            for dp in datapoints:
                labels = []
                for label in dp.labels.all():
                    labels.append(label.name)
                tmp.write(str(dp.data) + ',' + ",".join(labels) + '\n')     
            tmp.seek(0)  
            content = smart_str(tmp.read())  
            res = HttpResponse(content, content_type='application/force-download') 
            res['Content-Disposition'] = 'attachment; filename=%s' % smart_str(tmp.name)
            res['Content-Length'] = len(content)
            # res['X-Sendfile'] = smart_str(tmp.name)
            return res
        return render(request, 'lab/error_csv.html', {})
