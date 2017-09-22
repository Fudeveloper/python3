from django.shortcuts import render
from django.http import JsonResponse
from booktest.models import *


# Create your views here.

def pro(request):
    return render(request, 'booktest/pro.html')


def pro2(request):
    pro_list = AreaInfo.objects.filter(parea_id=0)
    data = []
    for area in pro_list:
        data.append([area.id, area.title])
    return JsonResponse({'data': data})


def city(request, id):
    id = int(id)
    city_list = AreaInfo.objects.filter(parea_id=id)

    data = []
    for area in city_list:
        data.append({'id': area.id, 'title': area.title})
    return JsonResponse({'data': data})

