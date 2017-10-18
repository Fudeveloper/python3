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
    url(r'^air_pump/$', views.air_pump, name='air_pump'),

    # 环境监控
    url(r'^fresh_air/$', views.fresh_air, name='fresh_air'),
    url(r'^exhaust/$', views.exhaust, name='exhaust'),

    url(r'^humiture/$', views.humiture, name='humiture'),
    url(r'^leakage/$', views.leakage, name='leakage'),
    url(r'^lighting/$', views.lighting, name='lighting'),

    url(r'^smoke/$', views.smoke, name='smoke'),
    url(r'^protection/$', views.protection, name='protection'),
    # 销售管理

    url(r'^customer/$', views.customer, name='customer'),
    url(r'^order/$', views.order, name='order'),

    # 生产数据
    url(r'^bom/$', views.bom, name='bom'),
    url(r'^basic_data/$', views.basic_data, name='basic_data'),
    url(r'^technology/$', views.technology, name='technology'),
    url(r'^archives/$', views.archives, name='archives'),

    # 生产管理
    url(r'^scheduling/$', views.scheduling, name='scheduling'),

    url(r'^purchase/$', views.purchase, name='purchase'),
    url(r'^depute/$', views.depute, name='depute'),
    url(r'^rate/$', views.rate, name='rate'),

    # 采购管理

    url(r'^supply/$', views.supply, name='supply'),
    url(r'^buy/$', views.buy, name='buy'),
    # 库存管理
    url(r'^material/$', views.material, name='material'),
    url(r'^finished/$', views.finished, name='finished'),
    url(r'^accessories/$', views.accessories, name='accessories'),

    # 安保监控
    url(r'^people/$', views.people, name='people'),
    url(r'^video/$', views.video, name='video'),


    # 小功能块
    # 发送邮件
    url(r'^send_email/$', views.send_email, name='send_email'),

    # 警报灯
    url(r'^start_warn/$', views.start_warn, name='start_warn'),
    url(r'^stop_warn/$', views.stop_warn, name='stop_warn'),


    # 风扇
    url(r'^start_fan/$', views.start_fan, name='start_fan'),
    url(r'^stop_fan/$', views.stop_fan, name='stop_fan'),

    # 照明灯
    url(r'^start_light/$', views.start_light, name='start_light'),
    url(r'^stop_light/$', views.stop_light, name='stop_light'),



    url(r'^recv_data/$', views.recv_data, name='recv_data'),
    url(r'^test/$', views.test, name='test'),
    url(r'^cam/$', views.cam, name='cam'),


]
