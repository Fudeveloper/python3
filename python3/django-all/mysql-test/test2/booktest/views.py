from django.shortcuts import render, redirect
from booktest.models import BookInfo
# Create your views here.
from django.http import HttpResponse


# def index(request):
#     res = BookInfo.books1.filter(id__lt=5)
#     context = {'res': res}
#     return render(request, 'booktest/login.html', context)


def test(request):
    i = request.method
    return HttpResponse(request.path)


def get_test1(request):
    return render(request, 'booktest/get_test1.html')


def get_test2(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    context = {'a': a, 'b': b, 'c': c}
    return render(request, 'booktest/get_test2.html', context)


def get_test3(request):
    a_list = request.GET.getlist('a')
    context = {'a': a_list}
    return render(request, 'booktest/get_test3.html', context)


def post_test1(request):
    return render(request, 'booktest/post_test1.html')


def post_test2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby_list = request.POST.getlist('uhobby')
    context = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby_list': uhobby_list}
    return render(request, 'booktest/post_test2.html', context)