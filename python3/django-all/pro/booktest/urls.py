from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^pro/$', views.pro, name='pro'),
    url(r'^pro2/$', views.pro2, name='pro2'),
    url(r'city(\d+)/', views.city, name='city'),

]
