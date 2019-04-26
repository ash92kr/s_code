# Django 월말평가 가이드 

준호쌤과 타키쌤 청문회를 통해 수집한 빅데이터를 기반으로 추측한 내용입니다.



## 🙆🏻‍♀️나옵니다

- 건드려야할 파일

  - views.py, templates, forms.py, (불확실 : admin.py)

- accounts
  - 회원가입, 로그인, 로그아웃

     - 회원가입 후 바로 로그인 상태로 전환

  - 유저의 상태 (로그인 or 로그아웃) 에 따라 분기

     ```python
      def login/signup(request):
      	if user.is_authenticated:
              return redirect('#')
     ```

- posts

  - CRUD

  - `post.user == user` 비교 (글 쓴 사람만 삭제 가능)

  - 좋아요 구현 ( + `{{ post.like_users.count }} 명이 좋아합니다`, `이 글을 좋아요한 유저 목록 for문` )

  - (불확실 : form 의 label 삭제)

    ```python
    class CommentForm(form.ModelForm):
    	content = forms.CharField(label="")
    	class Meta:
    		model = Comment
            fields = ['content', ]
    ```

- 기타
  - 데코레이터

  - from ~ import ~

  - 혹시 모르니까 `resolver_match`

    - 현재 페이지의 url name 을 이용해 제목/뒤로가기 분기

    ```html
    {% if request.resolver_match.url_name == 'create' %}
    	<h1>NEW</h1>
    {% else %}
    	<h1>EDIT</h1>
    {% endif %}
    ```

    



## 🙅🏻‍♀️안나와요

- 건드리지 말아야 할 파일
  - urls.py, models.py, settings.py 를 비롯한 기타 모든 파일
- 회원수정, 탈퇴, 비밀번호변경
- 이미지 업로드
- 유저 확장
- 팔로우
- forms.py 필드 인자 - widget
- custom form
- next 처리



