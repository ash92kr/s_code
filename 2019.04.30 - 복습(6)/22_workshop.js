const concat = (str1, str2) => `${str1} - ${str2}`

const checkLongStr = string => {
    if (string.length > 10) {
        return true
    } else {
        return False
    }
}

if (checkLongStr(concat('HAPPY', 'HACKING'))) {
    console.log('Long String')
} else {
    console.log('Short String')
}




const myObject = {
    key: 'Value',
}


myObject.key
myObject['key']






