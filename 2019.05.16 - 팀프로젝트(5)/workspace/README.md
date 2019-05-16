

## 대전 2반 1학기 프로젝트 보고서 - 빨간차(안상현, 정세민)





### 1. 완성된 소스코드의 Gitlab 주소

```
안상현 : https://lab.ssafy.com/ash92kr/final_project
정세민 : https://lab.ssafy.com/jho0078/project_final
```





### 2. 팀원 정보 및 업무 분담 내역

```
안상현 : 웹크롤링 및 데이터 수정, DB 설계, 프론트엔드(특히 댓글 CRUD 작성), 보고서 및 PPT 작성
정세민 : DB migration, 프론트엔드(특히 템플릿 설정, User Model 작성, 추천 알고리즘 작성), 발표
```



* 일정관리

![일정관리](https://user-images.githubusercontent.com/43332543/57840859-6454eb80-7804-11e9-8b3b-4992c2b73aa2.JPG)





### 3. 목표 서비스 구현 및 실제 구현 정도



전반적으로 필수 기능을 우선적으로 구현하는 데 목표를 두었다

##### (1) 관리자 권한의 유저만 화 등록 및 수정 / 삭제 권한을 가진다(별도의 관리자 권한 뷰가 구성되어야 함)

##### (2) 관리자 권한의 유저는 유저 관리 (수정 / 삭제 권한)을 가집니다. 

Django에서는 기본적으로 models.py를 설정하고 python manage.py createsuperuser를 입력하면 자동으로 admin 권한이 생성된다.

```python
# movies - admin.py
from django.contrib import admin
from .models import Movie, Actor, Genre, Comment

class MovieAdmin(admin.ModelAdmin):
    list_display =['actor1', 'poster_url', 'description', 'genre_id',] 

admin.site.register(Movie, MovieAdmin)
```



* 실제 템플릿 화면

![admin](https://user-images.githubusercontent.com/43332543/57841445-81d68500-7805-11e9-8faf-f9f986d61ecd.JPG)



##### (3) 모든 로그인 된 유저는 영화에 대한 평점을 등록 / 수정 / 삭제 등을 할 수 있어야 한다

```python
# movies - views.py

def comment_create(request, movie_pk):

def comment_delete(request, movie_pk, comment_pk):
    
def comment_update(request, movie_pk, comment_pk):

```



- 실제 템플릿 화면

![상세2](https://user-images.githubusercontent.com/43332543/57841043-cf9ebd80-7804-11e9-8dd8-1cdbd81301d3.JPG)

댓글 입력은 로그인 했을 때만 폼이 나오도록 구성했다.

댓글 수정과 삭제는 댓글을 단 사람만 가능하도록 구성했다.



##### (4) 평점을 등록한 유저는 해당 정보를 기반으로 영화를 추천 받을 수 있어야 한다

```python
# accounts - forms.py
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname','introduction','favorite_genre']
        
        FAVORITE_GENRE_CHOICE = (
            ('가족','가족'),('공포(호러)','공포(호러)'),('다큐멘터리','다큐멘터리'),('드라마','드라마'),
            ('멜로/로맨스','멜로/로맨스'),('뮤지컬','뮤지컬'),('미스터리','미스터리'),('범죄','범죄'),
            ('사극','사극'),('서부극(웨스턴)','서부극(웨스턴)'),('스릴러','스릴러'),('애니메이션','애니메이션'),('액션','액션'),
            ('어드벤처','어드벤처'),('전쟁','전쟁'),('코미디','코미디'),('판타지','판타지'),('SF','SF')
            )
            
        widgets = {
            'introduction': forms.Textarea,
            'favorite_genre': forms.Select(choices=FAVORITE_GENRE_CHOICE),
        }
```



* 실제 템플릿 화면

![메인화면](https://user-images.githubusercontent.com/43332543/57842136-e2b28d00-7806-11e9-8aa1-841d29e42516.JPG)

우리 팀은 유저가 가장 좋아한다고 선택한 장르의 영화를 추천해주는 기능을 구현했다.

선택한 장르의 영화 8개를 보여주되, 평점이 가장 높은 순서대로 정렬해서 로그인 시 첫 화면에 보여준다



##### (5) 데이터베이스에 기록되는 모든 정보는 유효성 검사를 진행해야 하며, 필요에 따라 해당하는 정보를 클라이언트 화면에 띄워줄 수 있어야 한다

#####  (6) HTTP method와 상태 코드는 적절하게 반환되어야 하며, 필요에 따라 해당하는 에러 페이지도 구성을 할 수 있다

```python
# movies - views.py
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Movie, Actor, Genre, Comment
from .forms import CommentForm
```



```python
# accounts - views.py

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
        
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_user = signup_form.save()
            Profile.objects.create(user=signup_user)
            auth_login(request, signup_user)
            return redirect('movies:list')
    else:
        signup_form = CustomUserCreationForm()
    context = {'signup_form': signup_form}
    return render(request, 'accounts/signup.html', context)
```



5번의 경우, movies와 accounts에 forms.py를 만들어 폼을 완성했다. 

이후 views.py에서 해당 폼을 거쳐 데이터를 입력, 수정, 삭제하는 경우(CUD), form.is_valid()를 통해 데이터가 누락되었는지, 해당 형식에 맞는지 등을 확인했다.

이러한 유효성 검사를 통과한 다음에야 form.save()를 통해 데이터를 DB에 저장했다.

또한, 수정(Update)은 기존에 유저가 입력한 내용을 보여주어야 한다.

이에 CommentForm(request.POST, instance=comment)과 같이 기존에 입력한 내용을 instance에 담아서 보여주도록 했다.



* 실제 템플릿 화면

![폼유효](https://user-images.githubusercontent.com/43332543/57842447-797f4980-7807-11e9-9bae-ca9b393ec029.JPG)



6번의 경우 get_object_or_404, get_list_or_404 라이브러리를 import해서 template에서 movie, comment 객체를 불러올 수 없는 경우 404 에러를 보여주도록 나타냈다.



* 실제 템플릿 화면

![에러](https://user-images.githubusercontent.com/43332543/57842259-1ee5ed80-7807-11e9-8325-846c0ceabc09.JPG)



##### (7) 그 외 추가적인 기능



###### 1) 검색 - 이용자가 키워드를 입력하면 키워드와 일치하는 영화 제목을 보여준다

```python
# movies - views.py

def movie_list(request):
    movies = Movie.objects.all()
    keyword = request.GET.get('keyword', '')
    if keyword: 
        movies = movies.filter(movie_name__icontains=keyword) 
    context = {
        'movies': movies
    }
    return render(request, 'movies/movie_list.html', context)
```



* 실제 템플릿 화면

![검색](https://user-images.githubusercontent.com/43332543/57842470-8dc34680-7807-11e9-9dff-79cc9984598e.JPG)





###### 2) 좋아요 - 유저가 특정 영화에 좋아요 버튼을 누르면 profile 페이지에서 그 영화의 이미지가 나옴

```python
# movies - views.py

@login_required
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
        liked = False
    else:
        movie.like_users.add(request.user)
        liked = True
    context = {
        'liked': liked,
        'count': movie.like_users.count(),
    }
    return JsonResponse(context)
```



* 실제 템플릿 화면

![좋아요](https://user-images.githubusercontent.com/43332543/57846154-88b5c580-780e-11e9-8780-3ee5f065f4a4.JPG)



###### 3) 팔로우 - 특정 유저의 동향이나 댓글을 파악하기 위해 버튼을 만듦



```python
# accounts - views.py
@login_required
def follow(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else:
        people.followers.add(request.user)
    return redirect('people', people.username)
```



* 실제 템플릿 화면

![follow](C:\Users\student\Desktop\follow.JPG)



### 4. 데이터베이스 모델링



![모델링](https://user-images.githubusercontent.com/43332543/57835902-89446100-77fa-11e9-8706-8139a73776eb.JPG)





### 5. 핵심 기능



(1) 검색 기능 : 이용자가 원하는 키워드를 입력하면 해당 키워드를 가진 영화명이 나온다

이후, 포스터 이미지를 클릭하면 해당 영화에 대한 상세 정보를 제공함

* 실제 템플릿 화면은 2-7-1에 있으므로 생략함



(2) 정보 제공 기능 : 영화 이미지를 클릭하면 웹크롤링한 정보가 모두 나온다

특히, 영화진흥위원회에서 가져온 영화 기본 정보, 네이버 영화 API에서 가져온 포스터 및 전체 평점, 유투브에서 가져온 동영상 링크 등을 한 자리에서 볼 수 있다





### 6. 배포 서버 URL

```
http://movies-dev.ap-northeast-2.elasticbeanstalk.com
```





### 7. 느낀 점

```
(1) 안상현 : 이전 프로젝트보다 처음부터 끝까지 모두 실행한다는 점에서 어려웠지만, 팀원의 도움으로 어려움을 극복할 수 있었다. 또한, 웹과 알고리즘을 결합시켜 하나의 결과물을 만들었다는 점에서 보람있었다. 개인 사정으로 하루 빠진 적이 있어서 다른 팀원이 보다 많은 양의 업무를 했다는 점에서 아쉬웠다. 이 자리를 빌어 고마움을 전한다.

(2) 정세민 : api를 통해 데이터를 받아 db에 넣는 것 부터 장고를 이용한 프론트엔드 구현까지 약 4개월동안 배웠던 모든 것들을 사용해 하나의 영화추천 사이트를 만들었다는 점이 굉장히 기쁘다. 진행 과정에서 어려운 점이 많았지만 팀원과의 협력을 통해 잘 이겨나갔던 것 같다. 다만 디자인적으로 완성된 사이트를 만들지 못했다는 점에 아쉬움이 남는다.
```

