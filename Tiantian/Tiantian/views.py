#——*——  coding:utf-8  ——*——
#@Time  ：2022/1/12 0:10
#@Author    ：WuRongGuang
#@File  :views.py.py
#@Software  :PyCharm
from django.http import HttpResponse
from django.template import Template,Context
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

def indexhtml(request,age):
    """
    编写一个html
    :param request:
    :return:
    """
    html = """
    <html>
        <head></head>
        <body>
            <h1>我是index页面</h1>
            <img src = "https://t7.baidu.com/it/u=1732966997,2981886582&fm=193&f=GIF">
        </body><br>
        姓名：{{ name }}<br>
        年龄：{{ age }}
    </html>
    """

    #返回一个响应对象
    # return HttpResponse(html)
    #渲染动态的数据
    #1.创建模板
    template_obj = Template(html)
    #2.构建动态数据
    parmas = {"name":"gutianle","age":age}
    content_obj = Context(parmas)

    result = template_obj.render(content_obj)
    return HttpResponse(result)


##模板的第一种调用方法
from django.template.loader import get_template
def getindex2(request):
    template_obj = get_template("index.html")
    parmas = {"name":"张三","age":20}
    result = template_obj.render(parmas)
    return HttpResponse(result)

##模板的第二种调用方法
from django.shortcuts import render_to_response
def getindex2(request):
    parmas = {"name":"李四","age":20}
    return render_to_response("index.html",parmas)

##模板的第三种调用方法
from django.shortcuts import render
def getindex(request):
    parmas = {"name":"王五","age":20}
    return render(request,"index.html",parmas)
