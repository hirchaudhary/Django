from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^testimonial$', views.test),
	url(r'^project$', views.project),
	url(r'^about$', views.about)
]
