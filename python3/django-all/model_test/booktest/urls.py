from django.conf.urls import url
from booktest import views
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^show_test', views.show_test, name='show_test'),
   url(r'^index2/$', views.index2, name='index2'),
   url(r'^user1/$', views.user1, name='user1'),
   url(r'^user2/$', views.user2, name='user2'),
   url(r'^zhuanyi/$', views.zhuanyi, name='zhuanyi'),
   url(r'^csrf1/$', views.csrf1, name='csrf1'),
   url(r'^csrf2/$', views.csrf2, name='csrf2'),
   url(r'^verify1/$', views.verify1, name='verify1'),
   url(r'^verify2/$', views.verify2, name='verify2')

]