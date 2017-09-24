from django.shortcuts import render


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


# 产品管理
def archives(request):
    return render(request, 'demo/product/archives.html')


def order_status(request):
    return render(request, 'demo/product/order_status.html')


def plan(request):
    return render(request, 'demo/product/plan.html')


def tech(request):
    return render(request, 'demo/product/tech.html')









def craftwork(request):
    return render(request, 'demo/base_product2.html')


def base(request):
    return render(request, 'demo/base.html')



def product(request):
    return render(request, 'demo/base_product.html')
