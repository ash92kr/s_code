

# JAVA script

2019-04-30



Chrome 브라우저를 기본으로 함.

가장 선호도 높고 점유율 높은 언어 - front와 back 구현 모두 가능



개발자도구 > Console창에서 실행해보자

```javascript
window.innerHeight
> 969

window.print()
> undefined

innerWidth
> 1412

innerHeight
> 969

window.open() 
Window {postMessage: ƒ, blur: ƒ, focus: ƒ, close: ƒ, parent: Window, …}
```





* 상수선언

  ```javascript
  const clap = '<p>짝!</p>'
  ```

* 변수선언

  ```javascript
  for (let i = 1; i <= 10; i++) {
      if i % 3 === 0) {
          document.write(clap); 
      } else {
          document.write(`<p>${i}</p>`);
      }
  }
  
  > 결과
  1
  2
  짝!
  4
  5
  짝!
  7
  8
  짝!
  10
  ```




* javascript 연산자

```javascript
let area = 5*4
undefined

area
20

let foo = 1>5
undefined

foo
false

// and : && , or : ||
let bar = (7 > 1) && (2 < 4)
undefined

bar
true

// 타입 확인
let type = typeof 'hi'
undefined

type
"string"

// 함수 생성
function square(num) {
    return num * num 
}
undefined
square(3)
9

// 객체 선언
let person = {
    name : 'song',
    gender : 'male',
    phone : '0101234567', 
    sayHello: function () {
        console.log('Hi! My name is ' + this.name)
    }
}
undefined

// 정보 확인
typeof person
"object"
console.log(person)
VM819:1 {name: "song", gender: "male", phone: "0101234567", sayHello: ƒ}gender: "male"name: "song"phone: "0101234567"sayHello: ƒ ()__proto__: Object
undefined

person.sayHello()
VM722:6 Hi! My name is song
undefined

person.name
"song"
person.phone
"0101234567"
```



* 일치 연산자 `===` 

  * 엄격한 비교
  * 메모리의 같은 객체를 가리키고, 같은 타입이고, 값도 같다.
  * 일치 연산자를 사용하는 것이 좋다.

* 동등 연산자 `===`

  * 형변환 비교
  * 메모리의 같은 객체를 가리키거나 같은 값을 갖도록 변환할 수 있다면 비교
  * 서로 다른 타입이면 비교하기 전에 같은 자료형으로 변환하여 비교( 1 == "1")
  * 골칫거리와 혼란을 야기할 수 있다.


- 예시

```javascript
let i = 0
undefined
while (i < 10) {
    console.log(i)
    i++
}

VM1041:2 0
VM1041:2 1
VM1041:2 2
VM1041:2 3
VM1041:2 4
VM1041:2 5
VM1041:2 6
VM1041:2 7
VM1041:2 8
VM1041:2 9

for (let number of [1, 2, 3, 4, 5]) {
    console.log(number)
}
VM1122:2 1
VM1122:2 2
VM1122:2 3
VM1122:2 4
VM1122:2 5


// 인덱스는 정확한 양의 정수 인덱스만 사용 가능
const numbers = [1, 2, 3, 4, ]
undefined
numbers[0]
1
numbers[-1]
undefined

numbers.length
4

// array 순서 바꾸기
numbers.reverse()
(4) [4, 3, 2, 1]
numbers.push('a')
5
numbers
(5) [4, 3, 2, 1, "a"]
numbers.pop()
"a"
numbers
(4) [4, 3, 2, 1]
numbers.unshift('a')
5
numbers
(5) ["a", 4, 3, 2, 1]
numbers.shift()
"a"
numbers
(4) [4, 3, 2, 1]

numbers
(4) [4, 3, 2, 1]
numbers.includes(1)
true
numbers.includes(5)
false
numbers.indexOf(3)
1
numbers
(4) [4, 3, 2, 1]
numbers.reverse()
(4) [1, 2, 3, 4]

numbers.join()
"1,2,3,4"
numbers.join('')
"1234"
numbers.join('-')
"1-2-3-4"
```



* array

```javascript
var books = ['Learning JS', 'Eloguent JS', ]
undefined
var comics = {
    'DC': ['Aquaman', 'Shazam', ],
    'Marvel': ['Captain Marvel', 'Endgame', ],
}
undefined
var bookShop = {
    books: books,
    comics: comics, 
}
undefined
bookShop
{books: Array(2), comics: {…}}
books: (2) ["Learning JS", "Eloguent JS"]
comics: {DC: Array(2), Marvel: Array(2)}
__proto__: Object
var bookShop = {
    books, 
    comics,
}
bookShop
{books: Array(2), comics: {…}}
books: (2) ["Learning JS", "Eloguent JS"]
comics: {DC: Array(2), Marvel: Array(2)}
__proto__: Object
```



```javascript
const jasonData = JSON.stringify({
    coffee: 'starbucks',
    icecream: 'mintchoco', 
})
undefined
jasonData
"{"coffee":"starbucks","icecream":"mintchoco"}"
typeof jasonData
"string"
const parseData = JSON.parse(jasonData)
undefined
parseData
{coffee: "starbucks", icecream: "mintchoco"}
typeof parseData
"object"
```



```javascript
// 함수 정의 1
function add(num1, num2) {
    return num1 + num2
}
undefined
// 함수 정의 2
const sub = function (num1, num2) {
    return num1 - num2
}
undefined

// 결과확인
add(1, 2)
3
sub(1, 3)
-2

typeof sub
"function"


```





```javascript
// arrow function
        // function과 중괄호를 줄이려고 고안된 단축 문법
        // 1. function은 생략해도 된다.
        // 2. 함수에 매개변수가 단 하나뿐이라면 ()도 생략 가능
        // 3. 함수 body(중괄호 안쪽)에 표현식이 하나라면 {}와 return 생략 가능
        const mul = function(num1, num2) {
            return num1 * num2
        }

        const mul = (num1, num2) => {
            return num1 * num2
        }
        // 주로 이렇게 많이 씀
        const mul = (num1, num2) => num1 * num2
        
// 예시2
var square = (num) => {
return num ** 2
}
undefined
var square = num => {
    return num ** 2
}
undefined
var square = num => num ** 2
undefined
```



```javascript
var noArgs = () => 'no args'
undefined
var noArgs
undefined
var noArgs= _ => 'no args'
undefined
var returnObj = () => {return { key: 'value'} }
undefined
var returnObj = () => ({key: 'value'})
undefined
```



* 인자에 키워드가 있는 경우에는 하나라도 소괄호를 생략할 수 없음.











## NodeJS

* nodejs 설치: <https://nodejs.org/ko/>

* 터미널에서 버전 확인

```javascript
student@DESKTOP MINGW64 ~
$ node --version
v10.15.3

student@DESKTOP MINGW64 ~
$ npm --version
6.4.1

student@DESKTOP MINGW64 ~/Desktop/js
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (js) chaewon
version: (1.0.0)
description:
entry point: (index.js)
test command:
git repository:
keywords:
author:
license: (ISC)
About to write to C:\Users\student\Desktop\js\package.json:

{
  "name": "chaewon",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}


Is this OK? (yes)

// 설치
student@DESKTOP MINGW64 ~/Desktop/js
$ npm install lodash
```



* Material Icon Theme 설치하면 VS code에서 아이콘 볼 수 있음~ 예쁘다!



* practice.js
* terminal에 실행 명령어

```javascript
// JS보다 좀더 편한 lodash
var _ = require('lodash')
let list = ['짜장면', '짬뽕', '볶음밥', ]
let numbers = _.range(1, 46)
let lottery = _.sampleSize(numbers, 6)

let pick = _.sample(list)
let menu =  {
    짜장면: 'http://dimg.donga.com/wps/ECONOMY/IMAGE/2017/04/14/83849831.3.jpg',
    짬뽕 : 'http://nimage.globaleconomic.co.kr/phpwas/restmb_allidxmake.php?idx=5&simg=201603280733335338976_20160328073458_01.jpg', 
    볶음밥 : 'http://recipe1.ezmember.co.kr/cache/recipe/2015/05/16/0748e83d9b7135ae2983247cf64c80bd1_m.jpg', 
}


console.log(`오늘의 메뉴는 ${pick}입니다!`)
console.log(menu[pick])

console.log(`행운의 번호: ${lottery}`)


let getMin = (a, b) => {
    if (a > b) {
        return b
    }
    return a
}

// if - else문 사용
// let getMin = (a, b) => {
//     let min;
//     if (a > b) {
//         min = b
//     } else {
//         min = a
//     }
//     return min
// }


let getMinFromArray = nums => {
    let min = Infinity   // 양의 무한대, 다른 어떤 수보다 더 큼

    // nums 배경을 돌면서 min변수와 비교하여 최소 값을 찾는다.
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}
ssafy = [1, 2, 3, 4, 5]
console.log(getMinFromArray(ssafy))
```



* 결과보기 - terminal

```javascript
student@DESKTOP MINGW64 ~/Desktop/js
$ node practice
오늘의 메뉴는 짜장면입니다!
http://dimg.donga.com/wps/ECONOMY/IMAGE/2017/04/14/83849831.3.jpg
행운의 번호: 7,14,3,9,22,21
1
```

