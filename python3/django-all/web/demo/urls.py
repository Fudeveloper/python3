from django.conf.urls import url
from demo import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),

    # 动力监控
    url(r'^switch/$', views.switch, name='switch'),
    url(r'^distribution_box/$', views.distribution_box, name='distribution_box'),
    url(r'^dynamo/$', views.dynamo, name='dynamo'),

    # 环境监控
    url(r'^exhaust/$', views.exhaust, name='exhaust'),
    url(r'^fresh_air/$', views.fresh_air, name='fresh_air'),
    url(r'^humiture/$', views.humiture, name='humiture'),
    url(r'^leakage/$', views.leakage, name='leakage'),
    url(r'^lighting/$', views.lighting, name='lighting'),
    url(r'^protection/$', views.protection, name='protection'),

    # 产品管理
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^order_status/$', views.order_status, name='order_status'),
    url(r'^plan/$', views.plan, name='plan'),
    url(r'^tech/$', views.tech, name='tech'),





    url(r'^base/$', views.base, name='base'),
    url(r'^product/$', views.product, name='product'),
    url(r'^craftwork/$', views.craftwork, name='craftwork'),


]
