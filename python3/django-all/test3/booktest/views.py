import os
import json
from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from booktest.models import *
from django.core.paginator import *

# Create your views here.
def index(request):
    return render(request, 'booktest/base.html')


def upload_pic(request):
    return render(request, 'booktest/upload_pic.html')

from django.conf import settings
def upload_handler(request):
    pic1 = request.FILES['pic1']
    pname = os.path.join(settings.MEDIA_ROOT, pic1.name)
    with open(pname, 'wb') as pc:
        for i in pic1.chunks():
            pc.write(i)
    # return render(request, 'booktest/upload_handler.html')
    return HttpResponse('<img src="/static/media/{0}">'.format(pic1.name))


def hero_list(request, page_index):
    if page_index == '':
        page_index = '1'
    hero_list = HeroInfo.objects.all()
    paginator = Paginator(hero_list, 3)
    page = paginator.page(int(page_index))
    # print(page_index)
    context = {'page': page}
    return render(request, 'booktest/list_hero.html', context)


def area(request):
    return render(request, 'booktest/area.html')


def area2(request, id):
    id = int(id)
    print(id)
    if id == 0:
        data = AreaInfo.objects.filter(parea_id=id)
    else:
        data = [{}]
    print(data)
    data_list = []
    for area in data:
        data_list.append([area.id, area.title])

    # print(data_list)

    return JsonResponse({"data_list": data_list})

