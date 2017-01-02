from django.conf.urls import url

from lab.controllers.AddDatapointController import AddDatapointController
from lab.controllers.AddDatapointLabelController import AddDatapointLabelController
from lab.controllers.AsCsvController import AsCsvController
from lab.controllers.FileImportController import FileImportController
from lab.controllers.SearchController import SearchController
from lab.controllers.AddEntityController import AddEntityController
from lab.controllers.AsUadetController import AsUadetController
from lab.controllers.DatapointController import DatapointController
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'datapoints/$', views.datapoints, name='datapoints'),
    url(r'datasets/$', views.datasets, name='datasets'),
    url(r'import/$', views.imports, name='import'),
    url(r'^file-upload/$', FileImportController.as_view(), name='file_upload'),
    url(r'settings/$', views.settings, name='settings'),
    url(r'search/$', SearchController.as_view(), name='settings'),

    url(r'^labels/$', views.labels, name='labels'),
    url(r'^label/(?P<label_id>\d{1,16})$', views.label_details, name='label_details'),
    url(r'edit_labels/(?P<datapoint_id>\d{0,16})/$', views.edit_labels, name='edit_labels'), # change this url to /datapoints/#id/labels
    url(r'add_datapoint/$', AddDatapointController.as_view(), name='add_datapoint'),
    url(r'^datapoint/$', AddDatapointController.as_view(), name='add_datapoint'),
    url(r'^datapoint/(?P<datapoint_id>\d{0,16})$', views.datapoint_details, name='datapoint_details'),
    url(r'entities/$', views.entities, name='entities'),
    url(r'entities/(?P<entity_id>\d{0,16})/$', views.entity_detail, name='entity_detail'),
    url(r'add_entity/$', views.add_entity),

]
