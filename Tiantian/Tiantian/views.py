#——*——  coding:utf-8  ——*——
#@Time  ：2022/1/12 0:10
#@Author    ：WuRongGuang
#@File  :views.py.py
#@Software  :PyCharm
from django.http import HttpResponse
def index(request):
    """
    视图
    :param request:形参 包含了请求信息的请求对象
    :return: HttpResponse 响应对象
    """
    return HttpResponse("hello word")

def about(request):
    import time
    now_time = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S",now_time)

    return HttpResponse(now_time)

def retest(request,id):
    print(id)
    print(request)
    return HttpResponse("我是retest")

def retest1(request,year,city):
    result01 = "我%s年在%s"%(year,city)
    result = "我在%s"%city
    return HttpResponse(result01)