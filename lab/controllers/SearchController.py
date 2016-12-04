from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

import itertools

from lab.models import Datapoint

class SearchController(View):
    def get(self, request):
        # display a search box which POST's to the same url
        return render(request, 'lab/search.html', {})

    def post(self, request):
        # return search results
        query = request.POST.get('q', None)
        if query is not None:
            results_in_name = Datapoint.objects.filter(name__icontains=query)
            results_in_label = Datapoint.objects.filter(labels__name__contains=query)
            merged = list(itertools.chain(results_in_name, results_in_label))

            results = None

            if len(merged) > 0:
                results = merged

            return render(request, 'lab/search_result.html', { 'search_results': results, 'original_query': query })
        return HttpResponse('Query not understood')