from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


def index(request):
    uname = request.session.get('uname')
    # upwd = request.session.get('upwd')
    context = {'uname': uname}
    return render(request, 'booktest/index.html', context)


def login(request):
    return render(request, 'booktest/login.html')


def login_handler(request):
    request.session['uname'] = request.POST.get('uname')
    # request.session['uname'] =

    return redirect(reverse('main:index'))


def logout(request):
    request.session.flush()
    return redirect(reverse('main:index'))

