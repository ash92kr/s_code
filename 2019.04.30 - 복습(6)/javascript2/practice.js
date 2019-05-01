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