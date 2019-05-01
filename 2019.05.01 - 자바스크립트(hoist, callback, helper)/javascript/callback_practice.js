// 배열로 이루어진 숫자들을 모두 더하는 함수
// numbers = [1, 2, 3, 4, 5,]

// const numbersAddEach = numbers => {
//     let sum = 0
//     for ( const number of numbers) {  // 반복문, 상수 생성
//         sum += number
//     }
//     return sum
// }

// numbersAddEach(numbers)
// console.log(numbersAddEach(numbers))

// // 배열로 이루어진 숫자들을 모두 빼는 함수
// const numbersSubEach = numbers => {
//     let sub = 0
//     for (const number of numbers) {
//         sub -= number
//     }
//     return sub
// }

// numbersSubEach(numbers)
// console.log(numbersSubEach(numbers))


// // 배열로 이루어진 숫자들을 모두 곱하는 함수
// const numbersMulEach = numbers => {
//     let mul = 1
//     for (const number of numbers) {
//         mul *= number
//     }
//     return mul
// }

// numbersMulEach(numbers)
// console.log(numbersMulEach(numbers))


// // 축약본
// // 숫자로 이루어진 배열의 요소들은 각각 [?, ?]한다.
// const numbersEach = (numbers, callback) => {
//     let acc
//     for (const number of numbers) {
//         acc = callback(number, acc) // [??]한다 = 콜백
//     }
//     return acc
// }


// // 더한다
// const addEach = (number, acc = 0) => {
//     return acc + number
// }
// numbersEach(numbers, addEach)
// console.log(numbersEach(numbers, addEach))

// // 뺀다
// const subEach = (number, acc = 0) => {
//     return acc - number
// }
// numbersEach(numbers, subEach)
// console.log(numbersEach(numbers, subEach))

// // 곱한다
// const mulEach = (number, acc = 1) => {
//     return acc * number
// }
// numbersEach(numbers, mulEach)
// console.log(numbersEach(numbers, mulEach))


// 익명함수화(임시변수 삭제하는 1회용 함수)
// numbersEach 이후의 제어들을 함수 정의 없이 매번 자유롭게 하기
const NUMBERS = [1, 2, 3, 4, 5,]  // 상수화

const numbersEach = (numbers, callback) => {
    let acc
    for (let i = 0; i < numbers.length; i++) {
        number = numbers[i]
        acc = callback(number, acc)
    }
    return acc  // 출력
}
                                                    // 일회용 함수
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc = 1) => acc * number))
