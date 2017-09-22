from django.shortcuts import render

# Create your views here.
# 请求首页
def index(request):
    return render(request, 'demo/index.html')