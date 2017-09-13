from django.shortcuts import render
# from django.http import *
# from django.http import response
# from django.template import RequestContext,loader\
from booktest.models import *
# Create your views here.


def index(request):
    # temp = loader.get_template('booktest/login.html')
    # return HttpResponse(temp.render())
    # book_list = BookInfo
    # book_list = [1, 2, 3]
    bookList=BookInfo.objects.all()
    b = BookInfo()
    b.btitle='123'
    context={'list':bookList}
    return render(request,'booktest/login.html',context)


def show(request, book_id):
    book = BookInfo.objects.get(pk=book_id)
    hero_list = book.heroinfo_set.all()
    context = {'list': hero_list}
    return render(request, 'booktest/show.html',context)