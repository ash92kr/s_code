// let 블록 스코프 예제
// {
//     let x = '정운지'
//     console.log(x)  // 정운지
//     {
//         let x = 1
//         console.log(x) // 1
//     }
//     console.log(x)  // 정운지
// }
// // console.log(x) // undifined error
// console.log(typeof x)  // undifined로 출력




// {
//     var x = '정운지'
//     console.log(x)  // 정운지
//     {
//         var x = 1
//         console.log(x) // 1
//     }
//     console.log(x)  // 1 -> 전역변수의 오염
// }
// // console.log(x) // undifined error
// console.log(typeof x)  // number로 출력됨


// let foo
// let bar = undefined

// foo  // undifined(값을 할당하지 않음)
// bar  // undifined(undefined로 할당함)
// baz  // referenceError(baz is not defined)



// 내가 작성한 코드
// y
// var y = 1
// y


// JS가 이해한 코드
// var y   // 선언
// y
// y = 1
// y  // 1


// 2(입력 코드)
// if (x !== 1) {
//     console.log(y)  // undefined(y를 끌어올려 선언만 함)
//     var y = 3
//     if (y === 3) {
//         var x = 1
//     }
//     console.log(y)   // 3
// }
// if(x === 1) {
//     console.log(y)   // 3
// }


// // javascript의 이해
// var y
// var x

// if (x !== 1) {
//     console.log(y)  // undefined(y를 끌어올려 선언만 함)
//     y = 3
//     if (y === 3) {
//         x = 1
//     }
//     console.log(y)   // 3
// }
// if(x === 1) {
//     console.log(y)   // 3
// }



// 3(입력코드)
// var x = 1
// if (x === 1) {
//     var x = 2  
//     console.log(x)  // 2
// }
// console.log(x)  // 2(함수가 없어서 전체 변수에 영향을 줌)
// // var로 변수를 선언하면 JS는 같은 변수를 여러번 정의해도 무시한다

// // 자바 스크립트의 이해
// var x
// x = 1

// if (x === 1) {
//     var x = 2  // 할당
//     console.log(x)  // 2
// }
// console.log(x)



// 함수 호이스팅
// ssafy 함수가 선언되기 전에 ssafy()로 호출된 형태

ssafy()

// function ssafy() {
//     console.log('hosting!')
// }

let ssafy = function() {
    console.log('hosting!')
}


