from django.db import models


# # Create your models here.
# # 动力监控表
# class Power(models.Model):
#     # 开关
#     open = models.BooleanField(default=False)
#     # 名称
#     pname = models.CharField(max_length=20)
# 
#     def __str__(self):
#         return self.pname
# 
# 
# # 精密配电柜表
# class Distribution(models.Model):
#     # 电流
#     current = models.FloatField()
#     # 负载电流
#     load_current = models.FloatField()
#     # 名称
#     pname = models.CharField(max_length=20)
# 
#     def __str__(self):
#         return self.pname
# 
# 
# # 支路配电开关状态表
# class BranchSwitch(models.Model):
#     open = models.BooleanField(default=False)
#     # 名称
#     pname = models.CharField(max_length=20)
# 
#     def __str__(self):
#         return self.pname
#
#
# # 环境监控表
# class Environmant(models.Model):
#     # 新风机
#     wind = models.CharField(max_length=30)
#     # 排风机
#     exhaust = models.CharField(max_length=30)
#     # 温度
#     temperature = models.FloatField()
#     # 湿度
#     humidity = models.FloatField()
#     # 厂房内灯状态
#     light_open = models.BooleanField(default=False)
#     # 名称
#     pname = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.pname
#
#
# # 防雷监测表
# class LightningProtect(models.Model):
#     # 需要具体数据
#     pname = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.pname
#
#
# # 安保监控表
# # class
#
#
# # 产品档案表
# class Product(models.Model):
#     # 产品名
#     pname = models.CharField(max_length=30)
#     # 产品简介
#     content = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.pname
#
#
# # 工艺管理表
# class Technology(models.Model):
#     pname = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.pname
#
#
# # 订单状态表
# class Order(models.Model):
#     # 订单号
#     order_id = models.IntegerField()
#     # 订单状态
#     state = models.CharField(max_length=20)
#     # 名称
#     pname = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.pname
#
#
# # 计划排产表
# class Plan(models.Model):
#     # 计划数量
#     plan_number = models.IntegerField()
#     # 已完成数量
#     finish_number = models.IntegerField()
#     # 名称
#     pname = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.pname
