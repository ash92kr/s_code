# project 11 Vue SPA





* 사전 작업

이 주소 복사하기 : <https://django-friday-sanghyeon2.c9users.io/api/v1/movies/>

Visual Code로 확인하기 : <file:///C:/Users/student/Desktop/2019.05.10/11_vue/index.html>

index.html의 자바스크립트는 app.js에 존재함



### (1) 데이터 요청



1.  Django Rest Framework로 개발한 Django API 서버에서 RESTful 하게 요청을 보내고 JSON 응답을 받아옵니다



* 우선 Cloud9에 다음을 입력하고 설치한다

```
pip install django-cors-headers
```



* settings.py

```
INSTALLED_APPS = [
	...
    'corsheaders',
]

MIDDLEWARE = [
	...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

...

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:9000'
)
```



* app.js

```
const app = new Vue({
  el: "#app",
  data: {
	...
    genres: [],
    movies: [],  // 현재 하드 타이핑 된 배열이지만, 실제로는 axios.get() 을 통해 API server 로 부터 받아옵니다.
 	...
  },
  methods: {
    getMovies: function () {
      axios.get('https://django-friday-sanghyeon2.c9users.io/api/v1/movies/')
        .then(response => response.data)
        .then(movies => {
          this.movies = movies.map(movie => {
            return { ...movie, newComment: ''}
          })
        })
        .catch(error => console.log(error))
    },
    ...
 },
 mounted: function () {
    this.getMovies()
 },
```



2.  API 에서 반드시 제공받아야 하는 정보는 장르정보, 화정보, 리뷰정보입니다. 추가로 다른 데이터를 제공받을 수 있습니다.



* serializers.py

```
from rest_framework import serializers
from .models import Genre, Movie, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name',]   # 'id'나 'name'은 필드명에 불과하므로 내 마음대로 이름 지정 가능

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score',]

class MovieSerializer(serializers.ModelSerializer):
    score_set = ScoreSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genre', 'score_set',]

class GenreDetailSerializer(serializers.ModelSerializer):
    movie_set = MovieSerializer(many=True)   # 이를 넣기 전에 먼저 선언해야 한다
    class Meta:
        model = Genre
        fields = ['id', 'name', 'movie_set',]  # movie_set 자체가 하나의 쿼리셋이므로 이중 쿼리셋이 됨
```





### (2) 페이지 레이아웃 설계



1. 영화 목록을 조회할 수 있는 UI -> 이미 제공됨



2. 영화 목록에서 특정 영화의 상세 정보를 조회할 수 있는 UI -> 이미 제공됨



3. 특정 영화에 리뷰와 평점을 작성할 수 있는 UI -> (3) - 2 - 2에서 만듦

```
<form>
                                    <label for="review">리뷰를 남겨주세요: </label>
                                    <input id="review" type="text" v-model="review.content">
                                    <input type="number" min="1" max="10" v-model="review.score">
                                    <button class="btn mr-5 btn-outline-success" @click="addReview(movieDetail)">남기기</button>
                                </form>
```



4.  영화 상세 정보와 함께 리뷰와 평점을 확인할 수 있는 UI

```
<div class="review-entry-box">
                                    <div class="review-entry" v-for="score in movieDetail.score_set">  <!--평점 객체 불러오기-->
                                        <p><b>Score: {{ score.score }}점</b> | {{ score.content }}</p>
                                    </div>
                                </div>
```



5. 장르별 영화 목록을 제공하는 버튼/링크 UI

```
<h6
                        class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
                        <span>장르별 보기</span>
                    </h6>
                    <ul class="nav flex-column mb-2" v-for="genre in genres">
                        <li class="nav-item mt-2">
                            <button class="btn btn-outline-secondary btn-block">{{ genre.name }}</button>
                        </li>
                    </ul>
```



1. 모든 영화정보를 조회한다



* index.html

```
<section v-show="!detailView" class="card-columns mt-3 container">
                        
                        <article v-for="movie in movies" class="card">
                            <img class="card-img-top" v-bind:src="movie.poster_url" alt="Card image cap">
                            <div class="card-body">
                                <h5 class="card-title">{{ movie.title }}</h5>
                                <p class="card-text">영화 평점 평균 : {{ (movie.score_set.reduce((total, x) => total + x.score/movie.score_set.length, 0)).toFixed(2) }}</p>
                                <p class="card-text">
                                    <small class="text-muted">누적 관객수 : {{ movie.audience }}</small>
                                </p>
                                <a href="#" class="btn btn-primary" @click="toggleDetail(movie.id, genres.name)">영화 상세보기</a>
                            </div>
                        </article>
                    </section>
```



2. 특정 영화의 다음과 같은 항목들을 조회합니다.

- 제목

```
<section v-show="detailView" class="mt-3 mb-5 container">
                        <header class="row">
                            <h1 class="my-4 col-9">{{ movieDetail.title }}</h1>
                            <div class="col-3 m-auto">
                                <button class="btn btn-danger " @click="toggleDetail()">뒤로가기</button>
                            </div>
                        </header>
```



* 평균 평점

```
<div class="col-md-8">
                                <h2 class="my-3">평점</h2>
                                <p>계산된 총 평점평균 : {{ movieDetail.avg }}</p>
```



* 누적 관객

```
<p class="card-text">
                                    <small class="text-muted">누적 관객수 : {{ movie.audience }}</small>
                                </p>
```



* 포스터 이미지 url

```
                        <div class="row">
                            <div class="col-md-4">
                                <img v-bind:src="movieDetail.poster_url" alt="random-movie-poster">
                            </div>
```



* 설명 및 장르

```
                            <div class="col-md-8 ">
                                <p>장르 : {{ movieDetail.genre }}</p>
                                <p>줄거리 : {{ movieDetail.description }}</p>
                            </div>
```



* app.js

```
const app = new Vue({
    el: "#app",
    data: {
      logo: 'MO<i class="fab fa-vuejs"></i>IE',
      isMain: true,
      HOST:'https://django-friday-sanghyeon2.c9users.io/api/v1',
      genres: [],
      movies: [],  // 현재 하드 타이핑 된 배열이지만, 실제로는 axios.get() 을 통해 API server 로 부터 받아옵니다.
      detailView: false, // 현재 방식의 목록/상세 화면 전환에 사용되는 flag 입니다.
      movieDetail: {  // 상세 화면에서 출력할 때 사용할 영화 객체입니다.
        score_set: [],
        avg: 0,
      },
      review: {
        content: '',
        score: 1,
      }
    },
    methods: {
      
      toggleDetail: function(id=null, genrename) {  // 목록 <=> 상세 화면을 전환합니다. 인자로 id 가 들어올 경우, 상세화면을 표시합니다.
        if (id) {
          const movie = this.movies[id-1]  // 현재는 무조건 $data.movies 의 첫 번째 영화를 선택합니다. 실제로는 인자로 넘어온 id 를 통해 특정 영화를 찾습니다.
  
          // Better way..?
          this.movieDetail = movie
          // this.movieDetail.score_set = []  // 상세 페이지에서 표시할 모든 $data.scores 를 받아와야 합니다.
          if (this.genres[movie.genre-1].name) {
            this.movieDetail.genre = this.genres[movie.genre-1].name // 해당 movie 의 genreId 를 통해 genre.name 을 찾아서 저장합니다.
          } else {
            this.movieDetail.genre = ''
          }
            this.movieDetail.avg = (movie.score_set.reduce((total, x) => total + x.score/movie.score_set.length, 0)).toFixed(2)
        }
        this.detailView = !this.detailView
      },
  
      addReview: function (movie) {
        axios.post(`${this.HOST}/movies/${movie.id}/scores/`, this.review)
        .then(response => response.data.message)
        .then(() => {
            // this.movieDetail.score_set.push(this.review)
            movie.score_set.push({...this.review})
            this.movieDetail.avg = (this.movieDetail.avg*1 + this.review.score/(movie.score_set.length+1)).toFixed(2)
            this.review.content=''
            this.review.score=1
        })
        .catch(error => console.log(error))
      }
    },
  
    created: function () {  // Vue 인스턴스가 생성되는 시점에 실행되는 함수입니다. 현재는 Vue 인스턴스가 생성되면, json-server 에서 장르목록만 받아옵니다.
        axios.get(`${this.HOST}/genres/`)  // 만약 json-server 를 사용하지 않거나 서버가 꺼져있다면 에러가 발생합니다.
          .then(res => this.genres = res.data)
        axios.get(`${this.HOST}/movies/`)
          .then(res => this.movies = res.data)
    }
  })
```





* 특정 영화에 대한 리뷰 정보들을 조회합니다.

```
<div class="col-md-8">
                                <h2 class="my-3">평점</h2>
                                <p>계산된 총 평점평균 : {{ movieDetail.avg }}</p>
                                <h3 class="my-3">리뷰</h3>
                                
                                <div class="review-entry-box">
                                    <div class="review-entry" v-for="score in movieDetail.score_set">  <!--평점 객체 불러오기-->
                                        <p><b>Score: {{ score.score }}점</b> | {{ score.content }}</p>
                                    </div>
                                </div>
```

