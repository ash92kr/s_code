## Django_06

**Content**

1. Model 1:N Relation
2. 추가 사항

> 190314 Thu 

---

### 1. Model 1:N Relation

> [MDN : Using models](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Models)

- 각각의 Comment 가 하나의 Board 에 관계된다.
- Board : Comment = 1 : N

#### 1.1 Comment Model

```python
# models.py
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    	# return f"<Board({self.board_id}: Comment({self.id})-{self.content}>"
```

> **모델관계**
>
> - ForeignKey : 일-대-다 ('일' 쪽이 key 를 포함)
> - OneToOneField : 일-대-일 (대부분 하나의 테이블로 통합함)
> - ManyToManyField: 다-대-다
>
> `on_delete`
>
> - ForeignKey 의 **필수 인자**이며, ForeignKey 가 참조하는 부모(Board) 객체가 사라졌을 때 거기 딸려있는 Comments 들을 어떻게 처리할지 정의 한다.
>
> - Database Integrity([무결성](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0_%EB%AC%B4%EA%B2%B0%EC%84%B1))을 위해서 매우 중요한 설정이다.
>   - 무결성은 우리가 앞에서 다뤘던 조건들이 해당된다. 
>
>   1. 개체 무결성 : 식별자는 Null 일 수 없고 중복일 수 없다. (PK, NOT NULL, UNIQUE)
>   2. 참조 무결성 : 릴레이션 관련된 설정 (모든 외래 키 값은 두 가지 상태 가운데 하나에만 속함을 규정)
>   3. 범위 / 도메인 무결성 : 컬럼은 지정된 형식을 만족해야한다. (Integer Datetime 등 / Not Null / Default / Check) 
>
> - 값에는 CASCADE, PROTECT, SET_NULL, SET_DEFAULT, SET(), DO_NOTING 가 있다. [doc](https://docs.djangoproject.com/ko/2.1/ref/models/fields/#arguments)
>
> > CASCADE : 부모객체가 삭제 됐을 때 이를 참조하는 객체도 삭제한다. (추천)
> >
> > PROTECT : 참조가 되어 있는 경우 오류 발생.
> >
> > SET_NULL : 부모객체가 삭제 됐을 때 모든 값을 NULL로 치환. (NOT NULL 조건시 불가능)
> >
> > SET_DEFAULT : 모든 값이 DEFAULT값으로 치환 (DEFAULT 설정 있어야함. DB에서는 보통 default 없으면 null로 잡기도 함. 장고는 아님.)
> >
> > SET() : 특정 함수 호출.
> >
> > DO_NOTHING : 아무것도 하지 않음. 다만, SQL에 on delete 직접 설정.

- migrate

```bash
$ python manage.py makemigrations boards
$ python manage.py showmigrations # migration 상태 확인
$ python manage.py migrate
```

- sqlmigrate 로 comment 의 migration 파일을 확인해보자

```bash
$ python manage.py sqlmigrate boards 0003
```

```sqlite
BEGIN;
--
-- Create model Comment
--
CREATE TABLE "boards_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" varchar(200) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "board_id" integer NOT NULL REFERENCES "boards_board" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "boards_comment_board_id_76b617ec" ON "boards_comment" ("board_id");
COMMIT;
```

> 여기서  `board_id` 라는 컬럼이 만들어진 것을 확인한다.
>
> 해당 댓글이 **몇 번째 글의 댓글인지** 알아야하기 때문에 comment 는 부모 board 의 id 값을 가지고 있다.
>
> (board 라는 이름의 컬럼으로 ForeignKey 를 만들었기 때문에 board_id 컬럼이 생성된 것이다. board 가 아닌 다른 변수명을 쓰면 $$$_id 식으로 만들어지지만 모델관계가 헷갈릴 수 있다. 그래서 **부모 클래스명의 소문자**로 사용하는 것이 좋다.)
>
> - boards_comment 테이블 모습
>
>   ```bash
>   $ sqlite3 db.sqlite
>   >> SELECT * FROM boards_comment;
>   ```
>
> |  id  | content | created_at | updated_at | board_id |
> | :--: | :-----: | :--------: | :--------: | :------: |
> |  .   |    .    |     .      |     .      |    .     |

- shell_plus 조작 및 확인

```bash
$ python manage.py shell_plus
```

```python
# 댓글 작성 및 저장

# 특정 게시글 불러오기
board = Board.objects.get(pk=1)

# 댓글 1
comment = Comment()
comment.content = 'first comment'
comment.board = board			# board 객체 자체를 넣는다. 실제 db 에는 board 의 id 가 저장된다.
comment.save()
comment.pk

# 댓글 2
comment = Comment(board=board, content='second comment')
comment.save()
comment.pk
```

- 관계 활용하기
  - board(일) -> comment(다) : `comment_set`
  - comment(다) -> board(일) : `board`

```python
# 가지고 있는 모든 댓글 가져오기
board = Board.objects.get(pk=1)
board.comment_set.all()
#=> <QuerySet [<Comment: Comment object (1)>]>

# 참조하는 게시글 확인하기
comment = Comment.objects.get(pk=1)
comment.board
#=> <Board: 1: lorem>

comment.board_id 		# 'board_pk' 는 attribute 오류
#=> 1
```

- admin 에 Comment 등록

```python
from .models import Board, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'board_id', )
admin.site.register(Comment, CommentAdmin)
```

#### 1.2 Create

> pk 가 앞으로 여러번 쓰이기 시작하기 때문에 명시적인 분류를 위해
>
> `board_pk`, `comment_pk` 로 바꿔서 사용하자. (기존 url, views 에 썼던 인자들도 모두 수정)

- create

```python
# views.py
from .models import Board, Comment

def comments_create(request, board_pk):
    # 댓글을 달 게시물
    board = Board.objects.get(pk=board_pk)

    # form 에서 넘어온 댓글 정보
    content = request.POST.get('content')

    # 댓글 생성 및 저장
    comment = Comment(board=board, content=content)
    comment.save()
    return redirect('boards:detail', board_pk)
	# return redirect('boards:detail', comment.board_id)
```

```python
# urls.py
path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
```

- new

```django
<!-- boards/detail.html -->
{% extends 'boards/base.html' %}
{% block body %}
	...
    <hr>
	<p>댓글 작성</p>
	<form action="{% url 'boards:comments_create' board.pk %}" method="POST">
        {% csrf_token %}
        comment: <input type="text" name="content">
        <input type="submit" value="submit">
	</form>
{% endblock %}
```

#### 1.3 Read

- 방법 1 (방법1,2 모두 보고 **2번**으로 진행)

```html
<!-- boards/detail.html -->
{% extends 'boards/base.html' %}
{% block body %}
	...
    <hr>

	{% for comment in board.comment_set.all %}
		<li>{{ comment.content }}</li>
	{% endfor %}

    <hr>

	<p>댓글 작성</p>
	...
{% endblock %}
```

- 방법 2

```python 
# views.py
def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    context = {
        'board': board,
        'comments': comments,
    }
    return render(request, 'boards/detail.html', context)
```

```html
<!-- boards/detail.html -->    
	{% for comment in comments %}
		<li>{{ comment.content }}</li>
	{% endfor %}
```

#### 1.4 Delete

> 방법 2 로 진행.

```python
# views.py
def comments_delete(request, board_pk, comment_pk):
    # 방법 1
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('boards:detail', board_pk)
    
    # 방법 2
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
    	comment.delete()
    	return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)
```

```python
# urls.py
path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
```

```html
<!-- 방법 1 -->
<!-- boards/detail.html -->
{% for comment in comments %}
	<li>
        {{ comment.content }}
        <a href="{% url 'boards:comments_delete' board.pk comment.pk %}">[삭제]</a>
	</li>
{% endfor %}
```

```html
<!-- 방법 2 -->
<!-- boards/detail.html -->
{% for comment in comments %}
	<li>
        {{ comment.content }}
		<form action="{% url 'boards:comments_delete' board.pk comment.pk %}" method="POST" onsubmit="return confirm('R U SURE?');" style="display: inline">
            {% csrf_token %}
            <input type="submit" value="삭제">
        </form>
	</li>
{% endfor %}
```

> 댓글 Update 는 페이지 흐름이 너무 복잡해지고, 일반적인 페이지처럼 만들기 위해서는 JS 가 필요하다.
>
> 후반부 JS 강의를 배우고 다시 돌아오자.

---

### 2. 추가 사항

#### 2.1 댓글 개수 보여주기

> `{{ comments | length }}`
>
> `{{ board.comment_set.all | length }}`
>
> `{{ comments.count }}` 는 count 메서드가 호출되면서 comment 모델 쿼리를 한번 더 보내줘야 하기 때문에 매우 작은 속도차이지만 더 느려진다.

```django
<!-- boards/detail.html -->
	...
	<p>댓글 작성 / {{ comments | length }} 개의 댓글</p>
	<form action="{% url 'boards:comments_create' board.pk %}" method="POST">
        {% csrf_token %}
        comment: <input type="text" name="content">
        <input type="submit" value="submit">
	</form>
{% endblock %}
```

#### 2.2 댓글 없을 때 다른 문장 출력하기

> `{% for in %}` `{% empty %}` `{% endfor %}`

```html
{% for comment in comments %}
	<li>
        {{ comment.content }}
        <form action="{% url 'boards:comments_delete' board.pk comment.pk %}" method="POST" onsubmit="return confirm('R U SURE?');" style="display: inline">
            {% csrf_token %} 
            <input type="submit" value="삭제">
        </form>
	</li>
{% empty %}
	<p><b>댓글이 없어요..</b></p>
{% endfor %}
```

---
