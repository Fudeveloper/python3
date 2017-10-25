from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import hashlib


# Create your views here.

def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')

    # 判断两次密码是否相同
    if pwd != cpwd:
        return redirect('/user/register/')

    # 密码加密
    s1 = hashlib.sha1()
    s1.update(pwd.encode('utf-8'))
    upwd_sha1 = s1.hexdigest()


    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = email
    user.save()

    # 注册成功转到登陆页面
    return redirect('/user/login/')

    # return HttpResponse()
    # return render(request,)
