# coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    # 获取数据库里面所拥有的BlogPost对象
    blog_list = BlogsPost.objects.all()
    hello = '欢迎来到我的博客'
    #render_to_response()返回一个页面(index.html)
    # 顺带把数据库中查询出来的所有博客内容（blog_list）也一并返回。
    return render_to_response('index.html', {'blog_list': blog_list,
                                             'hi': hello })