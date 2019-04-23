from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import hashlib
from .models import Board
from .forms import BoardForm

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {
        'boards': boards,
        'gravatar_url': gravatar_url,
    }
    return render(request, 'boards/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # board 를 바로 저장하지 않고, 현재 user 를 넣고 저장
            # 실제 DB 에 반영 전까지의 단계를 진행하고, 그 중간에 user 정보를
            # request.user 에서 가져와서 그 후에 저장한다.
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'boards/form.html', context)


def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)


def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:index')


@login_required
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)   
            if form.is_valid():
                board = form.save()                         
                return redirect('boards:detail', board.pk)
        else:
            form = BoardForm(instance=board)            
    else:
        return redirect('boards:index')
    context = {
        'form': form,
        'board': board,
    }
    return render(request, 'boards/form.html', context)
        


