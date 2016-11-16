from django.conf.urls import url
from . import views
from .AddDatapointView import AddDatapointView
from .CsvDownloader import CsvDownloader
from .DatapointLabelManager import DatapointLabelManager

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'edit_labels/(?P<datapoint_id>\d{0,16})/$', views.edit_labels, name='edit_labels'),
    url(r'add_datapoint/$', AddDatapointView.as_view(), name='add_datapoint'),
    url(r'entities/$', views.entities, name='entities'),
    url(r'^api/datapoints/as_csv/$', CsvDownloader.as_view(), name='download_as_csv'),
    url(r'^api/datapoint/(?P<datapoint_id>\d{0,16})/labels/$', DatapointLabelManager.as_view(), name='datapoint_label_manager'),
    url(r'^api/datapoint/as_image/(?P<datapoint_id>\d{0,16})/$', views.entity_image, name='entity_image'),
    url(r'^api/datapoint/as_image/(?P<datapoint_id>\d{0,16})/(?P<out_w>\d{0,5})/(?P<out_h>\d{0,5})/$', views.entity_image, name='entity_image'),
]
