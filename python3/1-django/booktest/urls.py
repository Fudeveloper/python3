from django.conf.urls import include, url
from booktest import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^(\d+)$', views.show)
]