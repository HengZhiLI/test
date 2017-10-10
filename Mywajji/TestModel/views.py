#coding=utf-8

from django.shortcuts import render
from django.db.models import Max
from models import *
from django.http import HttpResponse

def index(request):
    # list = BookInfo.books1.all()
    list = BookInfo.books1.aggregate(Max('bpub_date'))
    context={'list':list}
    return render(request,'TestModel/index.html',context)

def aaa(request,a):
    return HttpResponse(a)

def TestGet1(request):

    return render(request,'TestModel/TestGet1.html')

def TestGet2(request):

    a1 = request.GET['a']

    b1 = request.GET['b']

    c1 = request.GET['c']

    contex = {'a': a1, 'b': b1, 'c': c1}

    return render(request,'TestModel/TestGet2.html',contex)

def TestGet3(request):

    a = request.GET.getlist('a')

    contex = {'a':a}

    return render(request,'TestModel/TestGet3.html',contex)

def TestPost1(request):
    return render(request, 'TestModel/PostTest1.html')

def TestPost2(request):

    uname = request.POST['uname']
    upawd = request.POST['upawd']
    ugender = request.POST['ugender']
    uhoby = request.POST.getlist('uhobby')

    contex = {'uname':uname,'upawd':upawd,'ugender':ugender,'hobbys':uhoby}

    return render(request,'TestModel/PostTest2.html',contex)