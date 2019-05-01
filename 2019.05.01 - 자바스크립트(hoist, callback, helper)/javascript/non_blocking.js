// const nothing = () => {}


// console.log('start sleeping')
// setTimeout(nothing, 3000) // non-block -> 콜백 스택에서 3초 실행하고 있음(사용자 입장에서는 동기로 실행되는 듯이 보임)
// console.log('end of program')


// // python처럼 block을 하고 싶다면
// const logEnd = () => {
//     console.log('end of program')   // 콜백 함수에 실행문을 넣으면 3초 기다림
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000)


// 2
// function first() {
//     console.log('first')
// }

// function second() {
//     console.log('second')
// }

// function third() {
//     console.log('third')
// }

// first()
// setTimeout(second, 0)
// third()



// 연습문제
// func1()을 호출했을 때 아래와 같이 콘솔에 출력
// func1 -> func3 -> func2

function func1 () {
    console.log('func1')
    func2()
}

function func2 () {
    setTimeout(() => console.log('func2'), 2000)
    func3()
}

function func3 () {
    console.log('func3')
}

// func3(func1(setTimeout(func2, 0)))
func1()



