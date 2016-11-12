from django.shortcuts import render
from .models import Datapoint

# Create your views here.
def home(request):
    datapoints = Datapoint.objects.all()
    return render(request, 'lab/home.html', {'datapoints': datapoints})

