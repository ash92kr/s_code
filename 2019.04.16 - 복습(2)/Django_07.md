[TOC]

## Django_07

**Content**

0. static
1. Image Upload (Media)
2. MEDIA_ROOT
3. Image Resizing
4. Path of Uploaded Images

> 190320 Wed

---

### 0. static

> [Managing static files](https://docs.djangoproject.com/ko/2.1/howto/static-files/)
>
> [staticfiles settings](https://docs.djangoproject.com/ko/2.1/ref/settings/#settings-staticfiles)
>
> PROJECT03 을 BASE_PROJECT 사본 만들어두기

- 정적 파일
  - images, CSS, JS 등
- **정적 파일의 기본 경로**
  - `/APP_NAME/static/` 

`boards/static/boards` 에 실습용 이미지 파일을 올리고 template 에서 load 를 해본다.

```django
<!-- boards/index.html -->
{% extends 'boards/base.html' %}
{% load static %}
{% block body %}
    <h1>Board</h1>
    <img src="{% static 'boards/audrey.jpg' %}" alt="image"></img>
```

> 주로 html 태그 위쪽에 작성한다.
>
> 만약 템플릿 상속이 있다면, `{% extends '' %}` 가 가장 상단에 위치해야 한다.
>
> ```django
> {% extends '' %}
> {% load static %}
> <html>
> ```

- django 는 `/APP_NAME/static/` 안에서 상대적인 경로로 파일들을 찾는다.

  - 추가적인 app이 존재한다면 settings.py 의 INSTALLED_APP에서 정적 하위 디렉토리를 찾는다. (코드 순서대로)

- `{% static %}` 템플릿 태그는 정적 파일의 절대 URL을 생성한다.

- 추가적인 위치 혹은 임의의 경로에 정적 파일들을 놓고 싶다면, 정적 파일들이 어디에 있는지 django한테 알려주어야 한다. 

  ```python
  # settings.py
  STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'crud', 'assets'),
  ]
  ```

  > 반드시는 아니지만, 일반적으로 공용으로 사용되는 정적 파일들을 이곳(assets)에 놓는다. (ex. bootstrap, ... )

- `STATIC_URL` [[doc]](https://docs.djangoproject.com/ko/2.1/ref/settings/#static-url)

  - 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로. **이 최상위 경로 자체는 실제 파일이나 디렉토리가 아니고, URL로만 존재하는 단위.** 사용하고 싶은 URL로 마음대로 변경 가능하지만 그대로 사용 할 것이다.

  - 현재 프로젝트에서는 `http://주소/static/boards/이미지파일이름` 식으로 접속할 수 있다.

    ```PYTHON
    STATIC_URL = '/static/'
    ```

---

### 1. Image Upload (Media)

> [Model field reference](https://docs.djangoproject.com/ko/2.1/ref/models/fields/#module-django.db.models.fields)
>
> [FileField](https://docs.djangoproject.com/ko/2.1/ref/models/fields/#filefield)

#### 1.1 Model

- Board 모델에 새로운 컬럼 추가

  ```python
  class Board(models.Model):
      ...
      image = models.ImageField(blank=True)
  ```

  > 원래대로라면 새로운 컬럼을 추가하고 makemigrations 시에 어떤 값을 넣을건지 django 가 물어본다.
  >
  > `blank=True` 는 아무것도 안 들어가도 된다! 라는 의미이므로 makemigrations 시에 아무것도 물어보지 않는다.

  - image 컬럼 코드를 기존 컬럼 코드 사이에 넣어도 테이블에 추가 될 때는 제일 우측(뒤)에 추가된다.
    ([vscode 확장프로그램](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)이나 sqlmigrate 로 확인 가능)

- 모델 변경사항 적용

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  > migrations 에서 에러가 난다면 `pip install Pillow` 를 설치한다.

#### 1.2 Create

- column을 만들었으니 view 를 수정하고 template에 input을 추가 해보자.

  ```python
  # views.py
  def new(request):
      if request.method == 'POST':
          title = request.POST.get('title')
          content = request.POST.get('content')
          image = request.FILES.get('image')
  
          board = Board(title=title, content=content, image=image)
  		...
  ```

  ```django
  <!-- new.html -->
  ...
  <form method="POST" enctype="multipart/form-data">
  	...
      <input type="file" name="image" accept="image/*">
      <input type="submit" value="Submit"/>
  </form>
  ```

**HTML form enctype Attribute** [[doc]](https://www.w3schools.com/tags/att_form_enctype.asp)

- When you make a POST request, you have to encode the data that forms the body of the request in some way. (POST 요청을 할 때는 요청의 본문을 구성하는 데이터를 어떤 식으로든 인코딩해야 한다.)
- HTML form 이 제공하는 3가지 인코딩 메서드
  1. `application/x-www-form-urlencoded` : (기본값) 모든 문자 인코딩.
  2. `multipart/form-data` : 인코딩 하지 않음. 파일 업로드시 사용.
  3. `text/plain` : 공백은 "+" 기호로 변환하지만, 특수문자는 인코딩 하지 않음.
- `accept="image/*"` [[doc]](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input/file#%ED%97%88%EC%9A%A9%EB%90%9C_%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D_%EC%A0%9C%ED%95%9C%ED%95%98%EA%B8%B0)

  - 업로드시 이미지 파일만 업로드 하도록 설정
  - 파일 업로드시 선택목록을 필터링을 해준다. 하지만 파일 검증까지는 하지 못한다. (이미지만 accept 해놓아도 비디오나 오디오 파일을 제출 할 수 있다.)

#### 1.3 Read

- 이미지를 보여주는 태그 작성

  - `board.image.url` - 파일 주소
  - `board.image` - 파일 이름

  ```django
  <!-- boards/detail.html -->
  <!-- content 아래에 작성 -->
  <img src="{{ board.image.url }}" alt="{{ board.image }}"><br>
  ```

- 새로운 글을 작성해서 확인해보면 이미지가 로드되지 않고 이미지파일 위치가 이상한 곳(app, project, manage.py 와 동일 선상)에 업로드 된다. (개발자 도구로 엑박 이미지 확인)

- 왜?? settings.py에서 **MEDIA_ROOT** 설정을 해주지 않았기 때문이다. (현재 이미지는 django 가 보지 못하는 곳에 있다.)

---

### 2. MEDIA_ROOT

> [어떻게 이미지나 파일 필드를 사용할 수 있나요?](https://docs.djangoproject.com/ko/2.1/faq/usage/#how-do-i-use-image-and-file-fields)
>
> [MEDIA_ROOT](https://docs.djangoproject.com/ko/2.1/ref/settings/#media-root)

- 사용자가 올린 파일이 어디로 올라가는지 설정

- 이전에 `STATICFILES_DIRS` 를 설정 했던 것 처럼 경로 설정이 필요하며, 업로드 한 파일로 접근하는 URL도 설정이 필요

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- `MEDIA_URL` - `MEDIA_ROOT` 와 쌍으로 다니는 친구로 업로드 된 파일의 주소(URL)를 만들어 주는 역할을 한다.
  - `STATIC_URL ` 과 동일한 역할.
  - 아무 값이나 작성해도 된다. (ex. abc) 그러나 일반적으로 `/media/` 를 사용하기 때문에 변경하지 않는다.

```python
# crud/url.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# or
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 위에서 작성한 settings.py 설정을 바탕으로 업로드 된 파일의 주소 또한 만들어 준다. 업로드 된 파일을 가져오기 위해서는 그 파일에 접근하는 URL이 필요하다.
- 설정을 마친 후 처음에 올렸던 이미지 파일을 개발자도구 network 탭을 통해 요청경로를 확인해본다.
  - 경로가 `http://주소/media/sample_img.jpg` 로 바뀐 것을 볼 수 있다.
- 이제 new 페이지에서 게시글을 하나 등록하고 detail 페이지에서 사진이 잘 로드되는지 확인해본다. (+첫번째 이미지도 확인해본다.)
- 또한 이미지 파일도 `media` 폴더에 잘 업로드 되었는지 확인해본다. 
- `board.image.url` == `/media/sample_img.jpg`

> 이미지 파일이 어떻게 저장되는지 admin 페이지/shell_plus 에서 확인해보자.
>
> ```python
> class BoardAdmin(admin.ModelAdmin):
>  list_display = ['title', 'content', 'image', 'created_at', 'updated_at',]
> 
> admin.site.register(Board, BoardAdmin)
> ```
>
> ```bash
> # shell_plus
> 
> >>> board = Board.objects.get(pk=?)
> >>> board.image
> >>> dir(board.image)
> ```

> **같은 이름의 파일이 업로드**되면, django에서 파일명 뒤에 랜덤 문자열을 자동으로 붙여줘서 겹치지 않게 해준다.
>
> ex) `sample_img.jpg`, `sample_img_5oDwUzL.jpg` ..

> 이미지 수정은요?
>
> - 이미지도 edit 페이지를 통해 새로운 이미지로 수정할 수 있지만, text 와는 다르게 수정시 이미지를 무조건 업로드하지 않으면 오류가 발생한다.
> - `<input type="file">` 이 value 값을 지원하지 않기 때문에 댓글 수정처럼 추후에 자바스크립트를 통해 배울 예정이다.
>
> [MDN input type file](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input/file) / [Stackoverflow](https://stackoverflow.com/questions/1696877/how-to-set-a-value-to-a-file-input-in-html)

#### 2.1 추가사항

- 여기까지 했을 때 작은 문제가 있는데, 이미지 작업 없이 올렸던 이전 게시물들의 detail 페이지가 image 속성을 읽어오지 못해 페이지를 띄우지 못한다.

- 아래처럼 if 문을 사용할 수 있다.

  ```django
  <!-- detail.html -->
  <!-- 방법 1 -->
  {% load static %}
  	...
      {% if board.image %}
          <img src="{{ board.image.url }}" alt="{{ board.image }}">
      {% else %}
          <img src="{% static 'boards/no_image.png' %}" alt="no_image">
      {% endif %}
  	...
  ```

  ```django
  <!-- 방법 2 -->
  	...
      {% if board.image %}
          <img src="{{ board.image.url }}" alt="{{ board.image }}">
      {% endif %}
  	...
  ```

---

### 3. Image Resizing

- detail 페이지를 보면 이미지가 원본 그대로 업로드 되었기 때문에 너무 크거나 작게 나온다.

- html img 태그에서 직접 사이즈를 조정 해줄 수도 있지만, 용량 문제도 있기 때문에 이미지 업로드 자체를 resizing 할 필요가 있다.

- resizing 은 `django-imagekit` 모듈을 이용한다.

  ```bash
  $ pip install Pillow
  $ pip install pilkit
  $ pip install django-imagekit
  ```

  > pilkit 은 Pillow 사전 설치 필요.
  >
  > django-imagekit 또한 pilkit 사전 설치 필요.
  >
  > [Pillow](https://pypi.org/project/Pillow/)

- 설치한 모듈을 프로젝트에 등록한다.

  ```python
  INSTALLED_APP = [
  		...
  		'imagekit',
  		...
  ]
  ```

- Model Field

  ```python
  from imagekit.models import ProcessedImageField
  from imagekit.processors import ResizeToFill
  
  ...
  
      image = ProcessedImageField(
                  upload_to='boards/images',							# 저장 위치
                  processors=[ResizeToFill(200, 300)],		# 처리할 작업 목록
                  format='JPEG',													# 저장 포맷
                  options={'quality': 90},								# 옵션
      				)
  ```

  > `processors` [[doc]](https://github.com/matthewwithanm/pilkit#processors>)
  >
  > - ResizeToFill - 지정한 사이즈를 맞추고 넘치는 부분을 잘라냄.
  > - ResizeToFit - 지정한 사이즈를 맞추고 남는 부분을 빈 공간으로 둠. (ex. display block 과 유사)
  >
  > **(참고)** `ProcessedImageField()`의 parameter로 들어가 있는 값들은 makemigrations 후에 변경이 되더라도 다시 makemigrations를 해줄 필요 없다. 바로바로 반영이 된다. 

- Migration

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  - 이제 서버를 실행하고 이미지를 업로드 해보자.
    - 다시 개발자도구로 이미지의 요청경로를 확인해보자(`http://주소/media/boards/images/sample_img.jpg`)
  - 주의할 점은 코드를 수정한 후 업로드 하는 이미지에만 위 설정이 적용된다. 기존의 이미지들은 변하지 않는다. **사진을 업로드하는 시점**에 이미지를 변환하고 저장하기 때문이다.
  - admin 페이지에서 이미지끼리 주소를 비교해보자.

---

### 4. Path of Uploaded Images

- 지금까지는 간단하게 `media/boards/images` 처럼 고정적인 폴더에 이미지가 업로드 되도록 작성했다.

- 이러면 하나의 폴더에 모든 이미지가 업로드되서 나중에 관리가 어렵고 보기에도 좋지 않다.

- 그래서 이미지가 업로드 되는 위치를 깔끔하게 만들어 보자.

  ```python
  # models.py
  
  def board_image_path(instance, filename):
      return f'boards/{instance.pk}/images/{filename}'
  
  class Board(models.Model):
      ...
      image = ProcessedImageField(
                  upload_to=board_image_path,
  				...
      )
  ```

- 이미지를 업로드 해보자. **하지만 문제가 있다.** `instance.pk` 는 처음 Board 작성시에는 pk가 없는 상태이기 때문에( `pk`가 `None`이라서) `media/boards/None` 폴더에 모이게 된다. (수정할 때는 존재하는 Board 라서 pk가 있기 때문에 해당 pk로 폴더가 생성되고 그곳에 파일이 잘 저장된다.)

- 그래서 실제 개발에서는 이렇게 작성을 잘 하지 않는다. 보통 `instance.user.pk` 또는 `instance.user.username` 처럼 업로드 한 사람의 정보로 **폴더를 구조화**하는 경우가 많다.

---





