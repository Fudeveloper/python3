from django.contrib import admin

# Register your models here.
from demo.models import *


# Power
# Distribution
# BranchSwitch
# Environmant
# LightningProtect
# Product
# Technology
# Order
# Plan


@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]


@admin.register(BranchSwitch)
class BranchSwitchAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]


@admin.register(Environmant)
class EnvironmantAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]


@admin.register(LightningProtect)
class LightningProtectAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = [
        'pname'
    ]
