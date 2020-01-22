# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from . import models


def index(request):
    return HttpResponse("hello,world")


def book(request):
    book1 = models.Book.objects.get(pk=1)
    # 方法返回request,<页面>,dict类型返回给前端数据
    return render(request, 'index.html', {'book': book1})
