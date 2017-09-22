from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^upload_pic/$', views.upload_pic, name='upload_pic'),
    url(r'^upload_handler/$', views.upload_handler, name='upload_handler'),
    url(r'^list_hero/(\d*)/$', views.hero_list, name='hero_list'),
    url(r'^area/$', views.area, name='area'),
    url(r'area/(\d+)/$', views.area2, name='area2'),

]