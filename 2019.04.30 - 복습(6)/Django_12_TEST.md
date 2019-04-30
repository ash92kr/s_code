[TOC]

## Django_12_TEST

**Content**

0. TDD
1. 시작하기
2. Test setting
3. Test Model
4. Test CRUD

> 190423 /  Tue

---

### 0. TDD

> [테스트 할 때는, 많이 할 수록 좋습니다.](https://docs.djangoproject.com/ko/2.1/intro/tutorial05/#when-testing-more-is-better)
>
> Test Driven Development
>
> 원칙
>
> - 모델 혹은 뷰별로 테스트 케이스를 나눈다.
> - 테스트를 하고 싶은 상황별로 테스트 메서드를 나눈다.
> - 메서드 이름은 실행하고 싶은 내용에 대한 설명을 담는다.
>
> 본 수업은 댓글/로그인 기능까지 기본 구현된 프로젝트에서 진행되었다.
>
> 완성된 코드를 통해 성공하는 것을 확인하면서 진행하자. 그리고 다양한 오류 상황을 발생 시킴으로써 코드가 통과하는지를 알아보자.

### 1. 시작하기

> [django_test_plus](https://github.com/revsys/django-test-plus#django-test-plus)

- Django 에서 기본적으로 제공하는 TestCase 보다 훨씬 더 간편한 method 활용이 가능하다.

  ```bash
  $ pip install django_test_plus
  ```

### 2. Test settings

- `assertEqual` 는 서로 같은지 비교하고, 다르다면 Error를 발생시킨다.

  ```python
  # boards/tests.py
  
  # from django.test import TestCase
  from test_plus.test import TestCase
  from django.conf import settings 
  
  class SettingsTest(TestCase):
      def test_01_settings(self):
          self.assertEqual(settings.USE_I18N, True)
          self.assertEqual(settings.USE_TZ, False)
          self.assertEqual(settings.LANGUAGE_CODE, 'ko-kr')
          self.assertEqual(settings.TIME_ZONE, 'Asia/Seoul')
  ```

- 테스트 코드는 class 를 생성하고 method 이름이 `test`  로 시작하기만 하면 알아서 실행된다.

  ```bash
  $ python manage.py test boards
  ```

- `USE_I18N = False` 로 바꾸고 오류 내용을 확인해보자.

  ```bash
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  F
  ======================================================================
  FAIL: test_01_settings (boards.tests.SettingsTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "/home/ubuntu/workspace/ssafy_project_test/boards/tests.py", line 11, in test_01_settings
      self.assertEqual(settings.USE_I18N, True)
  AssertionError: False != True
  
  ----------------------------------------------------------------------
  Ran 1 test in 0.001s
  
  FAILED (failures=1)
  Destroying test database for alias 'default'...
  ```

- `Fail` 이 발생하였다. 다시 원래대로 변경해서 오류가 없도록 만들자.

---

### 3. Test Model

- Board 객체의 출력값이 `Board1` 로 클래스에 pk 값이 붙은 형식으로 만들고자 한다.

- 그리고 오류가 발생할 경우 msg 를 출력할 수 있도록 한다.

  ```python
  class BoardModelTest(TestCase):
      def test_01_model(self):
          board = Board.objects.create(title='test title', content='test content')
          self.assertEqual(str(board), f'Board{board.pk}', msg='출력 값이 일치하지 않음')
  ```

  ```bash
  ERROR: test_01_model (boards.tests.BoardModelTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
  	...
    File "/home/ubuntu/.pyenv/versions/insta-venv/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line 298, in execute
      return Database.Cursor.execute(self, query, params)
  django.db.utils.IntegrityError: NOT NULL constraint failed: boards_board.user_id
  
  ----------------------------------------------------------------------
  Ran 1 test in 0.009s
  
  FAILED (errors=1)
  Destroying test database for alias 'default'...
  ```

- `E(errors)` 가 발생했다. errors 는 fail 과 다르게 코드 자체에 오류가 있었던 것이다.

- 오류 메세지를 보면 `NOT NULL constraint` 가 발생하였고, `boards_board` 테이블에 `user_id` 가 필요하다고 한다. 에러를 해결해보자.

  ```python
  class BoardModelTest(TestCase):
      def test_01_model(self):
          board = Board.objects.create(title='test title', content='test content', user_id=1)
          self.assertEqual(str(board), f'Board{board.pk}', msg='출력 값이 일치하지 않음')
  ```

  ```python
  F
  ======================================================================
  FAIL: test_01_model (boards.tests.BoardModelTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "/home/ubuntu/workspace/ssafy_project_test/boards/tests.py", line 21, in test_01_model
      self.assertEqual(str(board), f'Board{board.pk}', msg='출력 값이 일치하지 않음')
  AssertionError: 'test title' != 'Board1'
  - test title
  + Board1
   : 출력 값이 일치하지 않음
  
  ----------------------------------------------------------------------
  Ran 1 test in 0.002s
  
  FAILED (failures=1)
  Destroying test database for alias 'default'...
  ```

- models.py 에 `__str__` 설정이 되어있지 않아 오류가 발생한다.

  ```python
  # boards/models.py
  class Board(models.Model):
  		...
      
      def __str__(self):
          return f'Board{self.pk}'
  ```

- 테스트가 성공하는지 확인한다.

---

### 4. Test CRUD

#### 4.1 Create - GET

- 이전에 작성한 테스트 코드는 `model` 설정과 관련해서 물어본 것이다. 이번에는 직접 작성하는 과정이다.

- Create는 항상 기억해야 하는 것이 **form을 제대로 주느냐**이다. 

- 가장 기본은 `get_check_200` 이다.
  - 인자로 url의 name을 받아서 실행 시켜주며, `GET` 요청을 보내고, 상태코드 200을 확인한다.

```python
class BoardViewTest(TestCase):
		def test_01_get_create(self):
		    response = self.get_check_200('boards:create')
		    self.assertContains(response, '<form')
```

```bash
F
======================================================================
FAIL: test_01_get_create (boards.tests.BoardViewTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/ubuntu/workspace/ssafy_project_test/boards/tests.py", line 44, in test_01_get_create
    response = self.get_check_200('boards:create')
  File "/home/ubuntu/.pyenv/versions/insta-venv/lib/python3.6/site-packages/test_plus/test.py", line 232, in get_check_200
    self.response_200(response)
  File "/home/ubuntu/.pyenv/versions/insta-venv/lib/python3.6/site-packages/test_plus/test.py", line 177, in response_200
    self.assertEqual(response.status_code, 200)
AssertionError: 302 != 200
```

- 302, 200.. redirect 와 관련된 HTTP 상태코드이다.

- 현재 views 에 create view 를 보면 `@login_required` 가 있기 때문이다.

- 즉, 로그인한 상태에서 테스트를 해야 한다.

- user는 `make_user` 를 통해 만들 수 있고 로그인 상태에서 활용하기 위하여 컨택스트 매니저인 `with` 구문을 통해 로그인 상태의 테스트를 하자. [with구문](https://velog.io/@sjquant/%ED%8C%8C%EC%9D%B4%EC%8D%AC-context-manager-with%EA%B5%AC%EB%AC%B8%EC%9C%BC%EB%A1%9C-%EC%95%88%EC%A0%84%ED%95%9C-%EB%A6%AC%EC%86%8C%EC%8A%A4-%EA%B4%80%EB%A6%AC%EB%A5%BC-%ED%95%98%EC%9E%90.)

- 예전에 파일 open 할 때 했었던 것과 동일하다. 

- with문의 범위를 벗어날 때, 혹은 with문 내에서 예외가 발생하더라도 파일 종료를 보장해준다.

  - 해당 코드 블럭에서는 login 된 상태로 테스트를 진행한다.

  ```python
  class BoardViewTest(TestCase):
  		def test_01_get_create(self):
        user = self.make_user(username='test', password='qawsedrf!')
        with self.login(username='test', password='qawsedrf!'):
            response = self.get_check_200('boards:create')
            self.assertContains(response, '<form') 
  ```

- 통과는 했지만, 더 정확한 테스트는 내가 원하는 form을 제공하였느냐이다.

- 이것은 정확한 테스트가 아니다. 내가 모델 폼을 제대로 주는지 확인을 하도록 하자.

  ```python
  from .forms import BoardForm
  
  class BoardViewTest(TestCase):
  		def test_01_get_create(self):
  		    user = self.make_user(username='test', password='qawsedrf!')
  		    with self.login(username='test', password='qawsedrf!'):
  		        response = self.get_check_200('boards:create')
  		        self.assertIsInstance(response.context['form'], BoardForm)
  ```

- `response.context['form']` 은 우리가 `return render` 하는 과정에서 마지막에 넘겨주는 `context` 딕셔너리의 값을 뜻하는 것이다.

- 그리고 그것이 `BoardForm` 의 인스턴스와 같은지 확인한 것이다.

- 여기에서 **테스트 코드의 구조**에 대해서 알아보자. 

  - 테스트 코드는 보통 given/when/then의 구조를 가지고 있다.

  - <https://en.wikipedia.org/wiki/Given-When-Then>

  - 위의 코드를 구분해 본다면, 다음과 같이 나눠 볼 수 있다.

    ```python
    class BoardViewTest(TestCase):
    		def test_01_get_create(self):
    				# given
    		    user = self.make_user(username='test', password='qawsedrf!')
    				# when
    		    with self.login(username='test', password='qawsedrf!'):
    		        response = self.get_check_200('boards:create')
    						# then
    		        self.assertIsInstance(response.context['form'], BoardForm)
    ```

- 마지막으로, `login_required` 를 별도로 테스트하기 위해 추가하자.

  ```python
  def test_02_get_create_login_required(self):
      self.assertLoginRequired('boards:create')
  ```

#### 4.2 Create - POST

이제 글 작성을 해보자. 여기서 가장 기본적인 given/when/then 은 무엇 일까?

- given : 사용자와 작성한 글(데이터)
- when : 로그인을 해서 post 요청으로 `boards:create` 로 요청 보낸 경우
- then : 글이 작성되고, view 에 설정된 주소로 redirect 한다.
- 여기에서는 `POST` 요청을 보내야 하니 다음의 코드를 활용 해보자. 실제  `[request.POST]` 값은 `data`  딕셔너리를 활용하면 된다.

```PYTHON
    def test_03_post_create(self):
        # given 사용자와 작성한 글 데이터
        data = {'title': 'test title', 'content': 'test content'}
        # when 로그인을 해서 post 요청으로 해당 url 로 요청 보낸 경우
        with self.login(username='test', password='qawsedrf!'):
            # then 글이 작성되고, 페이지가 제대로 redirect 됐는지
            self.post('boards:create', data=data)
            self.response_302()
```

- 근데 항상 user를 만드는 과정이 반복되고 있다. `setUp` 메소드는 해당 클래스의 테스트 코드가 실행되는 과정에서 먼저 실행되어 공통적인 **given 상황을 구성**하기에 좋다. `make_user` 의 중복을 제거하자.

  ```python
  class BoardViewTest(TestCase):
      def setUp(self):
          self.user = self.make_user(username='test', password='qawsedrf!')
  
  		def test_01_get_create(self):
  				# given when
          with self.login(username='test', password='qawsedrf!'):
              response = self.get_check_200('boards:create')
  						# then
              self.assertIsInstance(response.context['form'], BoardForm)
  		
  		... 생략 ...
  
  		def test_03_post_create(self):
  	        # given
  	        data = {'title': 'test title', 'content': 'test'}
  	        # when 
  	        with self.login(username='test', password='qawsedrf!'):
  	            # then
  	            self.post('boards:create', data=data)
  							self.response_302()
  ```

#### 4.3 Modelform

- modelform도 점검할 수 있다. `BoardViewTest` 가 아니라 `BoardModelTest` 에 추가한다.

```python
class BoardModelTest(TestCase):
    def test_01_model(self):
        board = Board.objects.create(title='test title', content='test content', user_id=1)
        self.assertEqual(str(board), f'Board{board.pk}', msg='출력 값이 일치하지 않음')
    
    def test_02_boardform(self):
        # given
        data = {'title': '제목', 'content': '내용'}
        # when then
        self.assertEqual(BoardForm(data).is_valid(), True)
    
    def test_03_boardform_without_title(self):
        data = {'content': '내용'}
        self.assertEqual(BoardForm(data).is_valid(), False)
        
    def test_04_boardform_without_content(self):
        data = {'title': '제목'}
        self.assertEqual(BoardForm(data).is_valid(), False)
```

#### 4.4 Detail

- 다시 `BoardVIewTest` 로 돌아와서 이제 상세보기가 제대로 된 내용을 출력하는지 확인하자.

  - given : post가 작성되어 있는 경우
  - when :  해당 경로로 요청을 보내면,
  - then : 해당 오브젝트 내용을 보여줘야 한다. (제목과 내용을 출력한다고 가정하자.)

  ```python
      def test_04_detail_contains(self):
          # given
          board = Board.objects.create(title='제목', content='내용', user=self.user)
          # when then - check_200까지 하니까 when then
          self.get_check_200('boards:detail', board_pk=board.pk) 
  ```

  - 만약, 제목과 내용을 출력하는지 알아보기 위해서 다음과 같이 추가할 수도 있다.

    ```python
    def test_04_detail_contains(self):
        # given
        board = Board.objects.create(title='제목', content='내용', user=self.user)
        # when
        self.get_check_200('boards:detail', board_pk=board.pk)   
        # then
        self.assertResponseContains(board.title, html=False)
        self.assertResponseC
    ```

  - 지정된 템플릿을 사용했는지도 이름을 정해놓고 미리 체크 할 수 있다.

    ```python
    def test_05_detail_template(self):
        # given
        board = Board.objects.create(title='제목', content='내용', user=self.user)
        # when
        response = self.get_check_200('boards:detail', board_pk=board.pk) 
        # then
        self.assertTemplateUsed(response, 'boards/detail.html')
    ```

#### 4.5 Index

- when : 요청이 오면 / then : 200 전체 게시글이 정확하게 오는지.

- ```python
  def test_06_get_index(self):
      # given when then
      self.get_check_200('boards:index')
  ```

- 템플릿 또한 확인 가능하다.

  ```python
  def test_07_index_template(self):
      # when then
      response = self.get_check_200('boards:index')
      self.assertTemplateUsed(response, 'boards/index.html')
  ```

- boards 뭐리셋이 일치하는지도 확인 할 수 있다.

  ```python
  def test_08_index_queryset(self):
      # given - 글 2개 작성
      Board.objects.create(title='제목', content='내용', user=self.user)
      Board.objects.create(title='제목', content='내용', user=self.user)
      boards = Board.objects.all()
      # when
      response = self.get_check_200('boards:index')
      # then
      self.assertQuerysetEqual(response.context['boards'], boards)
  ```

  ```bash
  AssertionError: Lists differ: ['<Board: Board2>', '<Board: Board1>'] != [<Board: Board2>, <Board: Board1>]
  
  First differing element 0:
  '<Board: Board2>'
  <Board: Board2>
  
  - ['<Board: Board2>', '<Board: Board1>']
  ?  -               -  -               -
  
  + [<Board: Board2>, <Board: Board1>]
  
  ----------------------------------------------------------------------
  ```

- 쿼리셋의 정렬이 다르기 때문에 오류가 발생했다.

  ```python
  def test_08_index_queryset(self):
      # given - 글 2개 작성
      Board.objects.create(title='제목', content='내용', user=self.user)
      Board.objects.create(title='제목', content='내용', user=self.user)
      boards = Board.objects.order_by('-pk')	# 해당 코드 수정
      # when
      response = self.get_check_200('boards:index')
      # then
      self.assertQuerysetEqual(response.context['boards'], map(repr, boards))
  ```

  - `map(repr, boards)`
  - 이렇게 하는 이유는 ['<Board: Board1>'] 이렇게 보이기 때문. 각자 string 으로 변경해준다.

#### 4.6 Delete

- given : 주어진 board 의 pk

- when : 요청이 오면

- then : 삭제한다.

  ```python
  def test_09_delete(self):
      board = Board.objects.create(title='제목', content='내용', user=self.user)
      with self.login(username='test', password='qawsedrf!'):
          self.get_check_200('boards:delete', board_pk=board.pk)
  ```

  ```bash
  FAIL: test_09_delete (boards.tests.BoardViewTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "/home/ubuntu/workspace/ssafy_project_test/boards/tests.py", line 100, in test_09_delete
      self.get_check_200('boards:delete', board_pk=board.pk)
    File "/home/ubuntu/.pyenv/versions/insta-venv/lib/python3.6/site-packages/test_plus/test.py", line 232, in get_check_200
      self.response_200(response)
    File "/home/ubuntu/.pyenv/versions/insta-venv/lib/python3.6/site-packages/test_plus/test.py", line 177, in response_200
      self.assertEqual(response.status_code, 200)
  AssertionError: 302 != 200
  ```

- get 요청을 했으니 오류가 발생했다.

- 메소드 이름을 바꿔서 get일 때 405인지 확인하자.

  ```python
  def test_10_delete_get_405(self):
      # given
      board = Board.objects.create(title='제목', content='내용', user=self.user)
      # when then
      self.get('boards:delete', board_pk=board.pk)
  		self.response_405()
  ```

- `response_405` 는 방금 보낸 요청이 HTTP 상태코드 405를 주는지 확인할 수 있다.

- 이제 삭제되는지 확인하자.

  ```python
  def test_11_delete_post(self):
      board = Board.objects.create(title='제목', content='내용', user=self.user)
      with self.login(username='test', password='qawsedrf!'):
          self.post('boards:delete', board_pk=board.pk)
          self.assertEqual(Board.objects.count(), 0)
  ```

- 삭제 후 리다이렉트 url도 확인해보자.

- `assertRedirects` 는 방금 보낸 response와 url을 알 수 있는데 (하드 타이핑('boards/')도 가능하지만)

- reverse를 써보자! 실제 url path로 뒤집는 번역 작업이다.

  ```python
  def test_12_delete_redirect(self):
      # given
      board = Board.objects.create(title='제목', content='내용', user=self.user)
      # when
      with self.login(username='test', password='qawsedrf!'):
          response = self.post('boards:delete', board_pk=board.pk)
          # then
          self.assertRedirects(response, reverse('boards:index'))
  ```

- 삭제도 로그인 여부를 확인 하는 테스트를 해야 한다.

  ```python
  def test_13_delete_login_required(self):
      board = Board.objects.create(title='제목', content='내용', user=self.user)
      self.assertLoginRequired('boards:delete', board_pk=board.pk)
  ```

#### 4.7 Update

- given : 주어진 board 의  pk

- when : 요청이 오면

- then : 수정한다.

- Form 이 제대로 반환 되는지 확인한다.

- 수정은 instance 값이 포함되어 있는지도 확인해야 한다.

  ```python
  def test_14_get_update(self):
      board = Board.objects.create(title='제목', content='내용', user=self.user)
      with self.login(username='test', password='qawsedrf!'):
          response = self.get_check_200('boards:update', board.pk)
          self.assertEqual(response.context['form'].instance.pk, board.pk)
  ```

- 수정도 로그인 여부도 확인해야 할 필요가 있다.

  ```python
  def test_15_get_update_login_required(self):
      self.assertLoginRequired('boards:update', board_pk=1)
  ```

  