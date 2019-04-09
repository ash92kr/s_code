from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)
    
@login_required    
def create(request):
    # POST 요청이면 Form 데이터를 처리한다
    if request.method == 'POST':
        # binding 과정(폼의 유효성 체크를 할 수 있도록 해준다)
        form = BoardForm(request.POST)   # BoardForm이 사용자 요청을 받는다
        # form 유효성 체크 - 실패하면 else를 지나친다
        if form.is_valid():   # 폼 자체가 유효한지 한번 더 검사함
            # title = form.cleaned_data.get('title')  # 유효성 검사를 통과한 데이터
            # content = form.cleaned_data.get('content')
            # board = Board(title=title, content=content)
            # board.save()
            # 검증을 통과한 깨끗한 데이터를 form에서 가져와 board를 만든다
            # board = Board.objects.create(title=title, content=content)   # 유효성 검사를 통과해 save를 할 필요가 없다

            # board를 바로 저장하지 않고, 현재 user를 넣고 저장한다
            # 실제 DB에 반영하기 전까지의 단계를 진행하고, 중간에 user 정보를 request.user에서 가져와 그 후에 저장한다
            board = form.save(commit=False)  # 우리는 저장만 하면 된다(models의 속성을 그대로 가져오기 때문)
            board.user = request.user
            board.save()
            return redirect('boards:detail', board.pk)
    # GET 요청(혹은 다른 메소드)이면 기본 폼을 생성한다
    else:
        form = BoardForm()  # Get이므로 요청이 없음
    context = {'form': form}  # 어떤 방식이든 form 자체는 출력되어야 한다
    return render(request, 'boards/form.html', context)
    
    
def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    context = {
        'board': board,
    }
    return render(request, 'boards/detail.html', context)
    

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    
    if board.user == request.user:
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:index')
        
@login_required 
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    
    if board.user == request.user:
        if request.method == "POST":
            form = BoardForm(request.POST, instance=board)    # 1
            if form.is_valid():
                # board.title = form.cleaned_data.get('title')
                # board.content = form.cleaned_data.get('content')
                # board.save()
                board = form.save()   # 2
                return redirect('boards:detail', board_pk)
    # GET 요청이면(수정하기 버튼을 눌렀을 때)
        else:
            # BoardForm을 사용자 입력 값을 넣어준 상태로 초기화한다
            form = BoardForm(instance=board)
        # form = BoardForm(initial=board.__dict__)  # board에 딕셔너리로 저장된 입력값을 불러옴
        # form = BoardForm(initial={'title': board.title, 'content': board.content})  # 위와 같음
    # context의 form은 상황에 따라 다르다
    # 1. POST : 요청에서 검증이 실패했을 때 오류 메시지가 포함된 상태다
    # 2. GET : 요청에서 초기화된 상태
    else:
        return redirect('boards:index')
    context = {'form': form, 'board': board,}
    return render(request, 'boards/form.html', context)  # create의 form을 그대로 사용할 수 있다
        
        
        