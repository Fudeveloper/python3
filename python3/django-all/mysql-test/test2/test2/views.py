from django.shortcuts import render
from booktest.models import BookInfo
# Create your views here.


def index(request):
    res = BookInfo.books1.filter(id__lt=5)
    context = {'res': res}
    return render(request, 'booktest/login.html', context)