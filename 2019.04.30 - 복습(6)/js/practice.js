var _ = require('lodash');
let list = ['짜장면', '짬뽕', '볶음밥',]
let numbers = _.range(1, 46)
let lottery = _.sampleSize(numbers, 6)
let pick = _.sample(list)
let menu = {
    짜장면:'http://pds21.egloos.com/pds/201504/06/41/d0021441_552156313afa7.jpg',
    짬뽕: 'http://pds21.egloos.com/pds/201510/26/41/d0021441_562d940c23677.jpg',
    볶음밥:'https://i.ytimg.com/vi/jpL3_pemotI/maxresdefault.jpg',
}

console.log(`오늘의 메뉴는 ${pick}입니다.`)
console.log(menu[pick])
console.log(`행운의 번호: ${lottery}`)


// let getMin = (a,b) => {
//     if (a > b) {
//         return b
//     }
//     return a
// }
// let getMin = (a,b) => {
//     let min;
//     if (a > b) {
//         min = b
//     } else {
//         min = a
//     }
//     return min
// }

let getMinFromArray = nums => {
    let min = Infinity  // 양의 무한대, 다른 어떤 수보다 더 큼.

    // nums 배경을 돌면서 min 변수와 비교하여 최소 값을 찾는다.
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}
ssafy = [1, 2, 3, 4, 5,]
console.log(getMinFromArray(ssafy))