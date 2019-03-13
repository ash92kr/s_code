from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    # boards = Board.objects.all()
    boards = Board.objects.order_by('-id')
    return render(request, 'boards/index.html', {'boards': boards})

def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()
    # return render(request, 'boards/create.html')
    return redirect('/boards/')
    
def detail(request, id):
    board = Board.objects.get(id=id)
    return render(request, 'boards/detail.html', {'board': board})

def delete(request, id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect('/boards/')

def edit(request, id):
    board = Board.objects.get(id=id)
    return render(request, 'boards/edit.html', {'board': board})

def update(request, id):
    board = Board.objects.get(id=id)   # 기존 것을 받아와서 덮어 씌움
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/detail/{ board.id }')