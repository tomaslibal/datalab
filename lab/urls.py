from django.conf.urls import url
from . import views
from .AddDatapointView import AddDatapointView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'edit_labels/(?P<datapoint_id>\d{0,16})/$', views.edit_labels, name='edit_labels'),
    url(r'add_datapoint/$', AddDatapointView.as_view(), name='add_datapoint'),
    url(r'^api/datapoint/as_image/(?P<datapoint_id>\d{0,16})/$', views.entity_image, name='entity_image'),
]
