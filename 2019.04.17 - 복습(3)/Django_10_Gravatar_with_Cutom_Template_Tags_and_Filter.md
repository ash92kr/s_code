[TOC]

## Django_10 : Gravatar with Custom template tags and filter

**Content**

1. Gravatar
2. Django Login Email 필드 추가
3. Custom template tags

> 190410 Wed

---

### 0. Gravatar

> https://ko.gravatar.com/

이메일을 활용하여 프로필 사진을 만들어주는 서비스.

한번 등록하면 이를 지원하는 사이트에서는 모두 해당 프로필 이미지로 사용할 수 있음.

먼저 내가 가입되어 있는지 아래 링크에서 이메일 체크를 해보고, 없다면 가입을 진행.

[https://ko.gravatar.com/site/check/wnsgh6315@gmail.com](https://ko.gravatar.com/site/check/wnsgh6315@gmail.com)

- 가입 후 자신의 이메일 주소를 위 링크에 넣고 URL로 들어가보면 기본 사진이 뜬다.

>  Footer의 `개발자 리소스`를 보면 이렇게 적혀있다.
>
>  - Gravatar 'API'는 인증이 필요하지 않습니다. HTTP GET 요청 하나로 모든 것을 처리할 수 있습니다. 아래의 링크를 통해 URL 요청 구조와 여러 종류의 다른 구현 방법을 찾을 수 있습니다.
>
>  - Creating the Hash
>
>   1. **Trim leading and trailing whitespace from an email address : `.strip()`**
>   2. **Force all characters to lower-case : `lower()`**
>   3. **md5 hash the final string : `import hashlib`**
>
>  ```python
>  import hashlib
>  hashlib.md5('hello@google.kr').hexdigest()
>  ```
>
>   - md5 암호화부터 해보자!
>   - 위 처럼 하면 python shell 에서 테스트시 인코딩 오류 발생
>
>  ```python
>  hashlib.md5('hello@google.kr'.encode('utf-8')).hexdigest()
>  ```
>
>   - 혹시 모를 공백과 대문자를 처리하자!
>
>  ```python
>  hashlib.md5('hello@google.kr'.encode('utf-8').lower().strip()).hexdigest()
>  ```
>
>  - Request Image
>
>  ```python
>  hash = hashlib.md5('hello@google.kr'.encode('utf-8').lower().strip()).hexdigest()
>  url = 'https://www.gravatar.com/avatar/{hash}'
>  ```

---

### 1. Django Login Email 필드 추가

1. 회원가입에서 사용했던 `UserCreationForm` 을 커스텀 해야한다. (기존 구조에 단순히 email 필드를 추가)

    이메일을 추가해야하니 기존 것에서 확장을 한다.

    > [UserCreationForm](https://docs.djangoproject.com/ko/2.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm)
    >
    > [Source code for django.contrib.auth.forms](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/)
    >
    > UserCreationForm() 은 기본적으로 password1, password2 필드를 가지고 있고 user model 을 통해 username 까지 3개의 필드를 가지고 있다.
    >
    > 우리가 만드는 UserCustomCreationForm 은 UserCreationForm 을 상속받기 때문에 fields에 password1 과 password2 를 명시하지 않아도 출력된다.
    >
    > 대신 user model 의 username 과 email 필드를 명시해야 한다.

    ```python
    # accounts/forms.py
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import get_user_model
    
    class UserCustomCreationForm(UserCreationForm):
        class Meta:
            model = get_user_model()
            fields = ['username', 'email',]
            # fields = ['username', 'password1', 'password2', 'email',]
    ```

2. 회원가입 view 수정

   ```python
    # accounts/views.py
    from .forms import UserCustomChangeForm, UserCustomCreationForm
    
    def signup(request):
        if request.user.is_authenticated:
            return redirect('boards:index')
    
        if request.method == 'POST':
            form = UserCustomCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('boards:index')
        else:
            form = UserCustomCreationForm()
        context = {'form': form}
        return render(request, 'accounts/auth_form.html', context)
   ```

3. gravatar 에 가입한 이메일과 동일한 이메일로 새로 회원가입을 해서 확인해보자.

    > `?s=80` 을 바꾸면서 사이즈 조절할 수 있음.

    ```django
    <!-- boards/base.html -->
    <body>
        <div class="container">
        {% if user.is_authenticated %}
            <h1>
                <img src="https://www.gravatar.com/avatar/d0e53a9a9bbc9cf481144a929930f41c?s=80">
                안녕, {{ user.username }}<br>
              ...
    ```

4. 그럼 이제 로그인 한 사람의 email 정보를 통해 동작해야 한다. 가장 간편한 방법은 파이썬에서 넘기는 것이다.

   ```python
    # boards/views.py
    import hashlib
    
    def index(request):
        if request.user.is_authenticated:
            gravatar_url = hashlib.md5(request.user.email.strip().lower().encode('utf-8')).hexdigest()
        else:
            gravatar_url = None # 변수 선언은 해야하니까 None 값을 할당.
        boards = get_list_or_404(Board.objects.order_by('-pk'))
        context = {
          'boards': boards, 
          'gravatar_url': gravatar_url,
        }
        return render(request, 'boards/index.html', context)
   ```

   ```DJANGO
   <!-- boards/base.html -->
   <body>
       <div class="container">
       {% if user.is_authenticated %}
           <h1>
               <img src="https://s.gravatar.com/avatar/{{ gravatar_url }}?s=80" alt="gravatar">
               안녕, {{ user.username }}<br>
   ```

   > 근데 base.html 에서 보이는 것인데 모든 views 함수에 context로 계산해서 넘겨줘야할까? 아니다.
   >
   > user는 독특하게 모든 request에 인스턴스가 있고, 이를 view, 그리고 템플릿에서 쓸 수 있다. 
   >
   > 이것만 암호화하면 된다.
   >
   > DTL에서 다양한 태그와 filter(`|`)를 했던 사용했는데 이건 template이 해야할 일이다.
   >
   > 그런데 기본 filter 값으로 hash 를 처리하는 것이 없기 때문에 직접 만들어보자.

---

### 2. Custom template tags

>  [Custom template tags and filters](https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/)

#### 2.1 Custom Tag 추가

- `[app_name]/templatetags` 폴더 생성(**폴더명은 반드시 `templatetags` !**)

        accounts/
            __init__.py
            models.py
            templatetags/
                __init__.py
                gravatar.py
            views.py

- `gravatar.py` 생성

    ```python
    # accounts/templatetags/gravatar.py
    import hashlib
    from django import template
    
    register = template.Library()  # 템플릿 라이브러리에
    
    @register.filter # 아래의 함수를 필터로 추가한다.
    def makemd5(email):
    		return hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
    ```

#### 2.2 Template 활용

- load 는 폴더에 생성한 python `파일명`이며, filter 에 쓰이는 것은 `함수명`이다.

    ```django
    {% load gravatar %}
    <img src="https://www.gravatar.com/avatar/{{ user.email|makemd5 }}?s=80">
    ```

    ```django
    <!-- boards/base.html -->
    {% load gravatar %}
    <!DOCTYPE html>
    ...
    <body>
        <div class="container">
        {% if user.is_authenticated %}
            <h1>
                <img src="https://s.gravatar.com/avatar/{{ user.email|makemd5 }}?s=150" alt="gravatar">
                안녕, {{ user.username }}<br>
    ```

- 동작이 잘 되는지 확인.
    - 그러면, 이제 필요 없어진 기존 코드를 지운다.

        ```python
        # boards/views.py
        def index(request):
            boards = get_list_or_404(Board.objects.order_by('-pk'))
            context = {
                'boards': boards,
                }
            return render(request, 'boards/index.html', context)
        ```

- gravatar 가입 안된 기본 디폴트 이미지가 별로면 다른 이미지들을 찾아 넣으면 된다.( `d=` )

- [https://ko.gravatar.com/site/implement/images/](https://ko.gravatar.com/site/implement/images/)
    - `외부 이미지 url` 혹은 `gravatar` 에 있는 것 쓸 수 있다.

      ```django
      <img src="https://www.gravatar.com/avatar/{{ user.email|makemd5 }}?s=150&d=https://ksassets.timeincuk.net/wp/uploads/sites/55/2016/07/2437349-pikachu-1.png">
      
      <img src="https://www.gravatar.com/avatar/{{ user.email|makemd5 }}?s=150&d=mp">
      ```


- **만약 코드에 문제가 없는데 이미지 변경이 안된다면 캐시 삭제+새로고침을 해보면 동작한다.**