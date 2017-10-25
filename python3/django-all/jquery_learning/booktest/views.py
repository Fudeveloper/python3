from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_test(request):
    p1 = request.GET.get('p1')
    if request.method == 'GET':

        return HttpResponse("get {0}".format(p1))
    else:
        return HttpResponse("not get")
