const axios = require('axios')

// const data = {
// 	"post": {
// 		"title": "Sample POST request2",
// 		"content": "Send this request via XMLHTTPRequest2",
// 		"author": "Master Tester2"
// 	}
// }

url = 'http://13.125.249.144:8080/ssafy/daejeon/2/posts'
// axios.post(url, data)

axios.get(url)
    .then(function(response) {
        console.log(response.data.posts)
    })
