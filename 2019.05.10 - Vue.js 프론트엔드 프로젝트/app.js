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