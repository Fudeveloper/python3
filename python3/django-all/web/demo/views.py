from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse


# Create your views here.
# 首页
def index(request):
    return render(request, 'demo/index.html')


# 动力监控
def switch(request):
    return render(request, 'demo/machine/switch.html')


def distribution_box(request):
    return render(request, 'demo/machine/distribution_box.html')

def dynamo(request):
    return render(request, 'demo/machine/dynamo.html')


def air_pump(request):
    return render(request, 'demo/machine/air_pump.html')


# 环境监控

def exhaust(request):
    return render(request, 'demo/envir/exhaust.html')


def fresh_air(request):
    return render(request, 'demo/envir/fresh_air.html')


def humiture(request):
    return render(request, 'demo/envir/humiture.html')


def leakage(request):
    return render(request, 'demo/envir/leakage.html')


def lighting(request):
    return render(request, 'demo/envir/lighting.html')


def protection(request):
    return render(request, 'demo/envir/protection.html')


def smoke(request):
    return render(request, 'demo/envir/smoke.html')


# 销售管理
def customer(request):
    return render(request, 'demo/sale/customer.html')


def order(request):
    return render(request, 'demo/sale/order.html')


# 生产数据
def bom(request):
    return render(request, 'demo/data/bom.html')


def basic_data(request):
    return render(request, 'demo/data/basic_data.html')


def technology(request):
    return render(request, 'demo/data/technology.html')


def archives(request):
    return render(request, 'demo/data/archives.html')


# 生产管理
def scheduling(request):
    return render(request, 'demo/product/scheduling.html')


def depute(request):
    return render(request, 'demo/product/depute.html')


def purchase(request):
    return render(request, 'demo/product/purchase.html')


def rate(request):
    # context = {''}
    return render(request, 'demo/product/rate.html')


# 采购管理
def buy(request):
    return render(request, 'demo/buy/buy.html')


def supply(request):
    return render(request, 'demo/buy/supply.html')


# 库存管理

def material(request):
    return render(request, 'demo/inventory/material.html')


def finished(request):
    return render(request, 'demo/inventory/finished.html')


def accessories(request):
    return render(request, 'demo/inventory/accessories.html')


def base(request):
    return render(request, 'demo/base/test.html')


# 邮件报警
def send_email(request):
    try:
        result = send_mail("警报！", "环境系统出现异常！", 'awo951127@sina.com', ['281138580@qq.com'])
    except Exception:
        result = '发送邮件出错，请联系管理员'

    return HttpResponse(result)

# 安保监控

def people(request):
    return render(request, 'demo/safe/people.html')

def video(request):
    return render(request, 'demo/safe/video.html')

# json传输处理
import json


def recv_data(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode())
    req = json.dumps({"data": "none"})
    return JsonResponse(req)


def test(request):
    return render(request, 'demo/test.html')


import requests
import json

# 报警灯
def start_warn(request):
    headers = {"Content-Type": "application/json"}

    jsondata = json.dumps({"head": "Set_Warning_light_Open"})

    result = requests.post('http://192.168.1.120:80/Handler1.ashx', data=jsondata, headers=headers)

    return HttpResponse(result)


def stop_warn(request):
    headers = {"Content-Type": "application/json"}

    jsondata = json.dumps({"head": "Set_Warning_light_Close"})

    result = requests.post('http://192.168.1.120:80/Handler1.ashx', data=jsondata, headers=headers)

    print(result.json())
    return HttpResponse(result)


# 风扇
def start_fan(request):
    headers = {"Content-Type": "application/json"}

    jsondata = json.dumps({"head": "Set_Fan_Open"})

    result = requests.post('http://192.168.1.120:80/Handler1.ashx', data=jsondata, headers=headers)

    return HttpResponse(result)


def stop_fan(request):
    headers = {"Content-Type": "application/json"}

    jsondata = json.dumps({"head": "Set_Fan_Close"})

    result = requests.post('http://192.168.1.120:80/Handler1.ashx', data=jsondata, headers=headers)

    print(result.json())
    return HttpResponse(result)

# 照明灯

def start_light(request):
    headers = {"Content-Type": "application/json"}

    jsondata = json.dumps({"head": "Set_Lighting_light_Open"})

    result = requests.post('http://192.168.1.120:80/Handler1.ashx', data=jsondata, headers=headers)

    return HttpResponse(result)


def stop_light(request):
    headers = {"Content-Type": "application/json"}

    jsondata = json.dumps({"head": "Set_Lighting_light_Close"})

    result = requests.post('http://192.168.1.120:80/Handler1.ashx', data=jsondata, headers=headers)

    print(result.json())
    return HttpResponse(result)


def cam(request):
    return render(request, 'demo/cam.html')

# Set_Fan_Open            开风扇"  DO0
# Set_Fan_Close              关风扇
# Set_Lighting_light_Open    开照明灯 	DO1
# Set_Lighting_light_Close   关照灯
# Set_Warning_light_Open     开报警灯     DO2
# Set_Warning_light_Close    关报警灯
