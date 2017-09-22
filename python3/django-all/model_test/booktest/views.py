from django.shortcuts import render
from booktest.models import HeroInfo
from django.http import HttpResponse

def index(requset):
    hero_list = HeroInfo.objects.all()
    context = {'hero_list': hero_list}
    return render(requset, 'booktest/base.html',context)

def show_test(request):
    return render(request, 'booktest/show_test.html')


def index2(request):
    return render(request, 'booktest/index2.html')

def user1(request):
    return render(request, 'booktest/user1.html')

def user2(request):
    return render(request, 'booktest/user2.html')

def zhuanyi(request):
    context = {'t1': '<a href="">123</a>'}
    return render(request, 'booktest/zhuanyi.html', context)


def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    context = {'uname': request.POST['uname']}
    return render(request, 'booktest/csrf2.html', context)

from django.http import HttpResponse
def show_verify(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import io as cStringIO
    buf = cStringIO.StringIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def verify1(request):
    return render(request, 'booktest/verify1.html')

def verify2(request):
    verify =  request.POST['verify']
    context = {'verify': verify}
    return render(request, 'booktest/verify2.html',context)