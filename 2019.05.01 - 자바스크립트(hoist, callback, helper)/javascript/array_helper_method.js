// 1. forEach
// forEach 함수는 아무것도 return하지 않는다.

// ES5(이전 버전)
var colors = ['red', 'blue', 'green',]

for (var i = 0; i < colors.length; i++) {
    console.log(colors[i])
}

// ES6+(현재 버전)
const COLORS = ['red', 'blue', 'green',]
COLORS.forEach(function (color) {  // color는 인자
    console.log(color)
})

COLORS.forEach(color => console.log(color))
// function을 지우고, 인자가 1개면 소괄호 지우고, {}는 =>로 대체


// 연습문제1 : 아래 함수의 for를 forEach로 바꾸시오
function handlePosts() {
    const posts = [
        { id: 43, title: 'daily news' },
        { id: 78, title: 'Code City' },
        { id: 108, title: 'The Ruby'},
    ]

    for (let i=0; i < posts.length; i++) {
        savePosts(posts[i])  // 존재하지 않는 함수이므로 출력이 안 됨
    }
}



function handlePosts() {
    const posts = [
        { id: 43, title: 'daily news' },
        { id: 78, title: 'Code City' },
        { id: 108, title: 'The Ruby'},
    ]

    posts.forEach(function (post) {
        savePosts(post)
    })
}


// 연습문제2 : 아래 코드의 images 배열 안에 있는 정보(height, width)를
// 곱해 넓이를 구하여 areas 배열에 저장하는 코드를 forEach 헬퍼를 사용해 작성하기

const images = [
    { height: 10, width: 30 },
    { height: 20, width: 40 },
    { height: 30, width: 60 },
]

const areas = []

images.forEach(function (image) {
    areas.push(image.height * image.width)
})

console.log(areas)


// 2.map
// map 함수는 새로운 배열을 return한다.(배열 요소를 변형)
// 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때
// map filter는 모두 사본을 return하며 원본 배열은 바뀌지 않는다.


const NUMBERS = [1, 2, 3,]
const DOUBLE_NUMBERS = NUMBERS.map(function (number) {
    return number * 2
})

// const DOUBLE_NUMBERS = NUMBERS.map( number => number * 2 )

console.log(DOUBLE_NUMBERS)


// 연습문제1 map 헬퍼를 사용해 images 배열 안의 Object들의
// height만 저장되어 있는 heights 배열에 저장해보자.

const images2 = [
    { height: 15, width: 30 },
    { height: 25, width: 40 },
    { height: 35, width: 60 },
]

const heights = images2.map( image => image.height)

// const heights = image2.map(function (image) {
    // return image.height
// })

console.log(heights)

// 연습문제2 : map 헬퍼를 사용해 distance / time을 저장하는 배열 speeds를 만들어보자
const trips = [
    { distance: 34, time: 10 },
    { distance: 90, time: 50 },
    { distance: 59, time: 25 },
]

const speeds = trips.map( trip => trip.distance / trip.time )

// const speeds = trips.map( function(trip) {
    // return trip.distance / trip.time
// })

console.log(speeds)


// 연습문제3 : 다음 두 배열을 객체로 결합한 coimcs 배열을 만들자.
// brands 요소가 key, movies 요소가 value

const brands = ["Marvel", "DC"]
const movies = ["IronMan", "BatMan"]

const comics = brands.map((x, i) => ({name: x, hero: movies[i]}))
// x는 brands 객체 값을 가져오며, i는 인덱스 번호(movies 객체의 해당 인덱스 값을 가져옴)
console.log(comics)


// 3.filter 
// filter 함수는 필터링 된 요소들만 배열로 return한다.
// 배열에서 필요한 것들만 남길 때 사용한다.
const PRODUCTS = [
    { name: 'cucumber', type: 'vegetable' },
    { name: 'banana', type: 'fruit' },
    { name: 'carrot', type: 'vegetable' },
    { name: 'apple', type: 'fruit' },
]

const fruitProducts = PRODUCTS.filter(function (product) {
    return product.type === 'fruit'  // product의 type이 fruit인 것의 name만 나옴
    // 해당 조건문에서 true를 만족할 경우만 새 배열에 넣는다
})
// const fruitProducts = PRODUCTS.filter( product => product.type === 'fruit')
console.log(fruitProducts)


// 3-1 filter 헬퍼를 사용해서, numbers 배열 중 50보다 큰 값들만 필터링해서 filteredNumbers 에 저장하라.
const numbers = [ 15, 25, 35, 45, 55, 65, 75, 85, 95 ]

const filteredNumbers = numbers.filter( number => number > 50)
console.log(filteredNumbers)


// 3-2 users 배열에서 admin 이 true 인 user object 들만 filteredUsers 배열에 저장하라.
const users = [
    {id: 1, admin: true},
    {id: 2, admin: false},
    {id: 3, admin: false},
    {id: 4, admin: false},
    {id: 5, admin: true},
]

const filteredUsers = users.filter( user => user.admin === true)
// return user.admin
console.log(filteredUsers) 







