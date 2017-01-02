from django.conf.urls import url

from lab.controllers.AddDatapointLabelController import AddDatapointLabelController
from lab.controllers.AsCsvController import AsCsvController
from lab.controllers.FileImportController import FileImportController
from lab.controllers.SearchController import SearchController
from lab.controllers.AddEntityController import AddEntityController
from lab.controllers.AsUadetController import AsUadetController
from lab.controllers.DatapointController import DatapointController
from . import views

urlpatterns = [
    url(r'api/entity/$', AddEntityController.as_view()),

    url(r'api/labels/(?P<label_id>\d{0,16})/usagenum/$', views.num_datapoints_use_label, name='num_datapoints_use_label'),
    url(r'api/label/(?P<label_id>\d{0,16})/delete/$', views.label_delete),

    url(r'^api/datapoint/(?P<datapoint_id>\d{0,16})$', DatapointController.as_view()),
    url(r'^api/datapoints/download/wswtm/$', AsCsvController.as_view(), name='download_as_csv'),
    url(r'^api/datapoints/download/uadet/$', AsUadetController.as_view()),
    url(r'^api/datapoint/(?P<datapoint_id>\d{0,16})/labels/$', AddDatapointLabelController.as_view(), name='datapoint_label_manager'),
    url(r'^api/datapoint/(?P<datapoint_id>\d{0,16})/delete/$', views.delete_datapoint),
    url(r'^api/datapoint/(?P<datapoint_id>\d{0,16})/label/(?P<label_id>\d{0,16})/delete$', views.delete_dp_label, name='datapoint_label_delete'),
    url(r'^api/datapoint/as_image/(?P<datapoint_id>\d{0,16})/$', views.entity_image, name='entity_image'),
    url(r'^api/datapoint/as_image/(?P<datapoint_id>\d{0,16})/(?P<out_w>\d{0,5})/(?P<out_h>\d{0,5})/$', views.entity_image, name='entity_image'),
]
