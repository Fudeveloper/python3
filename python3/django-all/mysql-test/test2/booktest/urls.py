"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from booktest import views
from booktest import view_login

urlpatterns = [
    # url(r'^index$', view_login.index, name='index'),
    url(r'^$', view_login.index, name='index'),


    url(r'^login_handler/$', view_login.login_handler, name='login_handler'),
    url(r'^login/$', view_login.login, name='login'),
    url(r'^logout/$', view_login.logout, name='logout'),


    url(r'^test/$', views.test, name='test'),
    url(r'^get_test1/$', views.get_test1, name='get_test1'),
    url(r'^get_test2/$', views.get_test2, name='get_test2'),
    url(r'^get_test3/$', views.get_test3, name='get_test3'),
    url(r'^post_test1/$', views.post_test1, name='post_test1'),
    url(r'^post_test2/$', views.post_test2, name='post_test2'),

    # url(r'^login/$', view_login.login, name='login')

]
