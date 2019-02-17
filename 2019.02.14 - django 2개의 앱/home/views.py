from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime

# Create your views here.
def index(request):   # 장고에서는 뷰 함수의 인자에 항상 request를 넣어야 한다
    # print(request)
    # print(type(request))
    # pprint(request.META)
    # return HttpResponse('Welcome to Django!')
    return render(request, 'home/index.html')

def dinner(request):
    
    menus = ['치킨돈부리', '라면', '맘스터치 싸이버거', '빵']
    pick = random.choice(menus)

    # return HttpResponse(one)
    return render(request, 'home/dinner.html', {'menus': menus, 'pick': pick})


def hello(request, name):
    return render(request, 'home/hello.html', {'name': name})


def cube(request, num):
    num3 = int(num) ** 3
    return render(request, 'home/cube.html', {'num': num, 'num3': num3})


def ping(request):
    return render(request, 'home/ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')   # 딕셔너리로 값을 보내고 받음
    return render(request, 'home/pong.html', {'data': data})
    
    
def user_new(request):
    return render(request, 'home/user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'home/user_create.html', {'nickname': nickname, 'pwd': pwd})
    
    
def template_example(request):
    my_list = ['치킨', '피자', '간짜장', '생맥주', '돈까스']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'orange', 'coconut']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'home/template_example.html',
                  {'my_list': my_list, 'my_sentence': my_sentence,
                   'messages': messages, 'empty_list': empty_list,
                   'datetimenow': datetimenow
                  })


def static_example(request):
    return render(request, 'home/static_example.html')



