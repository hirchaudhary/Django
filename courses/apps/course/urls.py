from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addCourse$', views.addCourse),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^confirm/(?P<id>\d+)$', views.confirm),
]
