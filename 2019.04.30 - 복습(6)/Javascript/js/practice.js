var _ = require('lodash');
let list = ['짜장면', '짬뽕', '볶음밥',]
let numbers = _.range(1, 46)
let lottery = _.sampleSize(numbers, 6).sort()
let pick = _.sample(list)
let menu = {
    짜장면: 'https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/aY5/image/WAShqbdQkyf6QCJOBnjSFWJNpF8.jpg',
    짬뽕: 'http://image.chosun.com/sitedata/image/201511/13/2015111301067_0.jpg',
    볶음밥: 'https://t1.daumcdn.net/cfile/tistory/9937593D5A3B420128',
}
console.log(`오늘의 메뉴는 ${pick}입니다.`)
console.log(menu[pick])
console.log(`행운의 번호: ${lottery}`)


/* 최솟값 구하기*/
let getMin = (a, b) => {
    if (a > b) {
        return b
    }
    return a
}
// 위 아래는 같다
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
    let min = Infinity
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}
ssafy = [1, 2, 3, 4, 5,]
console.log(getMinFromArray(ssafy))

const concat = (str1, str2) => `${str1} - ${str2}`
console.log(concat('hello', 'l'))

const checkLongStr = (string) => {
    if (string.length > 10) {
        return true
    } else {
        return false
    }
}
console.log(checkLongStr('aawefawefkhawlef'))

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING')
} else {
    console.log('SHORT STRING')
}