from django.shortcuts import render, redirect
from .models import Board   # 현재 폴더에 있는 models에서 Board class를 가져온다

# 모듈 import 순서(위부터 아래로)
# 1. 파이썬 표준 라이브러리 ex) os, random 등
# 2. core django : 장고 프레임워크에 내장되어 있는 것 ex) django.shortcuts
# 3. third party library : pip install로 설치한 것들 ex) django-extension, beautifulsoup
# 4. 장고 프로젝트 app  ex) .models 등


# Create your views here.
def index(request):
    # boards = Board.objects.all()   
    # boards = Board.objects.all()[::-1]  # 원래 결과를 파이썬이 변경하는 것
    boards = Board.objects.order_by('-id')  # DB가 애초에 정렬을 바꿔서 보내줌
    return render(request, 'boards/index.html', {'boards': boards})

def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    board = Board(title=title, content=content)   # DB의 title 컬럼에 title 내용을 넣음
    board.save()
    # Board.objects.create(title=title, content=content)  # 한 줄 완성
    
    # return render(request, 'boards/index.html')   # 그냥 이렇게만 적으면 페이지를 띄워주고 보여주지 않음
    return redirect('/boards/')   # url 작성
    # return redirect(index)  # 뷰 함수 이름을 작성
    
    # 위 방식에서 글이 보이지 않는 이유는 보여지는 페이지 자체는 index지만
    # index의 url로는 돌아가지 못했기 때문이다. 즉, 단순히 html문서만 보여준 것
    
    # create은 model에 record를 생성해라는 요청이므로 단순히 페이지를 달라고 하는
    # GET방식보다는 POST가 의미상 더 적절하다. 또한, 모델과 관련된 데이터이므로
    # url에 직접 보여지는 것은 좋지 않다.
    
def detail(request, pk):
    board = Board.objects.get(pk=pk)   # pk가 같은 하나의 인스턴스 가져오기
    return render(request, 'boards/detail.html', {'board': board})
    
def delete(request, pk):  # 어떤 글만 삭제할 것인가?
    board = Board.objects.get(pk=pk)   # Board의 pk에 있는 값이 url을 통해 넘어온 pk와 같은 것만 선택
    board.delete()
    return redirect('/boards/')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/edit.html', {'board': board})
    
def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')   # 새로운 값을 기존의 값에 넣기
    board.content = request.POST.get('content')
    board.save()   # 새로운 값을 넣고 저장해야 한다
    return redirect(f'/boards/{board.pk}/')



