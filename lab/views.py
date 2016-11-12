from django.shortcuts import render
from .models import Datapoint

# Create your views here.
def home(request):
    datapoints = Datapoint.objects.all()
    return render(request, 'lab/home.html', {'datapoints': datapoints})

def edit_labels(request, datapoint_id):
    datapoint = Datapoint.objects.filter(id=datapoint_id)
    return render(request, 'lab/edit_labels.html', {'datapoint': datapoint})

