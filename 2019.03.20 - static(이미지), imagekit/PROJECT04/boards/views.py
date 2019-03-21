from django.shortcuts import render, redirect
from .models import Board, Comment
from pprint import pprint   # 터미널에서 볼 때 사용

# Create your views here.
def index(request):
    pprint(request)
    pprint(type(request))
    pprint(dir(request))
    pprint(request.scheme)
    pprint(request.get_host())
    pprint(request.get_full_path())
    pprint(request.build_absolute_uri())
    pprint(request.META)
    pprint(request.method)
    
    boards = Board.objects.order_by('-pk')
    context = {  # context를 통해 딕셔너리를 html에 넣음
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)
    
def new(request):  # 함수가 하나 줄어들고 restful하게 바뀜
    if request.method == 'POST':
        # CREATE
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        board = Board(title=title, content=content, image=image)
        board.save()
        return redirect('boards:detail', board.pk)
    else:   
        return render(request, 'boards/new.html')
    
# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
    
#     board = Board(title=title, content=content)
#     board.save()
#     # return redirect(f'/boards/{ board.pk }/')
#     return redirect('boards:detail', board.pk)
    
def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    context = {
        'board': board,
        'comments': comments,
    }
    return render(request, 'boards/detail.html', context)
    
def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == "POST":
        board.delete()
        # return redirect('/boards/')
        return redirect('boards:index')
    else:  # 주소로 입력하면 detail 페이지가 보이도록 함
        return redirect('boards:detail', board.pk)
    
def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    
    if request.method == "POST":  # UPDATE
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:   # EDIT
        context = {
            'board': board,
        }
        return render(request, 'boards/edit.html', context)

# def update(request, pk):
#     board = Board.objects.get(pk=pk)
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     # return redirect(f'/boards/{ board.pk }/')
#     return redirect('boards:detail', board.pk)
    
def comments_create(request, board_pk):
    # 댓글을 달 게시물부터 찾기
    board = Board.objects.get(pk=board_pk)   # board의 pk와 comment의 board_pk가 일치하는 board를 가져옴
    
    # form에서 넘어온 comment data
    content = request.POST.get('content')
    
    # 댓글 생성 및 저장
    comment = Comment(board=board, content=content)   # Comment의 board에 board 객체 전체를 넣으면, 필요한 부분만 가져감
    comment.save()
    return redirect('boards:detail', board.pk)
        
        # 몇 번 게시글의 몇 번 댓글을 지워야 하는가?
def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)   # 현재 게시글을 보여줌
    else:
        return redirect('boards:detail', board_pk)
