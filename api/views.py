from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from lab.models import Datapoint, UserDefinedEntity, Label, Dataset

def delete_dp_label(request, datapoint_id, label_id):
    label = Label.objects.get(id=label_id)
    Datapoint.objects.get(id=datapoint_id).labels.remove(label)
    return HttpResponse('OK')

"""
returns how many datapoints use the given label
"""
def num_datapoints_use_label(request, label_id):
    num = Datapoint.objects.filter(labels__id__exact=label_id).count()
    response = HttpResponse(num, content_type="text/plain")
    return response   


def label_delete(request, label_id):
    Label.objects.filter(id=label_id).delete()
    return HttpResponse('OK', content_type="text/plain")



def entity_image(request, datapoint_id, out_w=32, out_h=32):
    # passed in arguments from django url are always strings
    out_w = int(out_w)
    out_h = int(out_h)
    datapoint = Datapoint.objects.get(pk=datapoint_id)
    pixels = datapoint.data.split(',')
    num_pixels = len(pixels)
    w = int(sqrt(num_pixels))

    response = HttpResponse(content_type="image/png")
    img = Image.new('RGB', (w, w))
    
    rgb = []
    for px in pixels:
        rgb.append((int(px), int(px), int(px)))

    img.putdata(rgb)
    img.thumbnail((out_w, out_h), Image.ANTIALIAS)
    img.save(response, "PNG")
    return response

