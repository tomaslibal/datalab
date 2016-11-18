from django.conf.urls import url

from lab.controllers.AddDatapointController import AddDatapointController
from lab.controllers.AddDatapointLabelController import AddDatapointLabelController
from lab.controllers.AsCsvController import AsCsvController
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'datapoints/$', views.datapoints, name='datapoints'),
    url(r'datasets/$', views.datasets, name='datasets'),
    url(r'import/$', views.imports, name='import'),
    url(r'settings/$', views.settings, name='settings'),

    url(r'^labels/$', views.labels, name='labels'),
    url(r'edit_labels/(?P<datapoint_id>\d{0,16})/$', views.edit_labels, name='edit_labels'), # change this url to /datapoints/#id/labels
    url(r'add_datapoint/$', AddDatapointController.as_view(), name='add_datapoint'),
    url(r'^datapoint/$', AddDatapointController.as_view(), name='add_datapoint'),
    url(r'entities/$', views.entities, name='entities'),
    url(r'entities/(?P<entity_id>\d{0,16})/$', views.entity_detail, name='entity_detail'),

    url(r'api/labels/(?P<label_id>\d{0,16})/usagenum/$', views.num_datapoints_use_label, name='num_datapoints_use_label'),
    url(r'^api/datapoints/as_csv/$', AsCsvController.as_view(), name='download_as_csv'),
    url(r'^api/datapoint/(?P<datapoint_id>\d{0,16})/labels/$', AddDatapointLabelController.as_view(), name='datapoint_label_manager'),
    url(r'^api/datapoint/as_image/(?P<datapoint_id>\d{0,16})/$', views.entity_image, name='entity_image'),
    url(r'^api/datapoint/as_image/(?P<datapoint_id>\d{0,16})/(?P<out_w>\d{0,5})/(?P<out_h>\d{0,5})/$', views.entity_image, name='entity_image'),
]
