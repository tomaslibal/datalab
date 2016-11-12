from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'edit_labels/(?P<datapoint_id>\d{0,16})/$', views.edit_labels, name='edit_labels'),
]
