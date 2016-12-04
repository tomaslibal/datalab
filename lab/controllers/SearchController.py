from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

class SearchController(View):
    def get(self, request):
        # display a search box which POST's to the same url
        return render(request, 'lab/search.html', {})

    def post(self, request):
        # return search results
        return HttpResponse('Not yet implemented')