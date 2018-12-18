# python 과거(2버전)

'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')
# one과 two가 각각 %s로 들어간다

# python 현재(3버전) - pyformat
'{} {}'.format('one', 'two')

name = '홍길동'
e_name = 'Hong Gil Dong'

print("안녕하세요. {}입니다. My name is {}.".format(name, e_name))

# 변수의 순서 바꾸기 - 처음의 변수가 0, 나중의 것이 1
print("안녕하세요. {1}입니다. My name is {0}.".format(name, e_name))
print("안녕하세요. {1}입니다. My name is {1}.".format(name, e_name))


# f-string python 3.6
print(f'안녕하세요. {name}입니다. My name is {e_name}')
# format 대신 f를 사용하고 변수명을 직접 입력한다


# 로또 뽑기 - print(오늘의 행운의 번호는 ~~~ 입니다.)

pool= []

for i in range(1, 46):
    pool.append(i)

print(pool)

import random
lotto = random.sample(pool, 6)

# print(sorted(lotto))
lotto2 = sorted(lotto)
print(lotto2)

print("오늘의 행운의 번호는 {}입니다.".format(lotto2))
print(f"오늘의 행운의 번호는 {lotto2}입니다.")


name = "홍길동"
print("안녕하세요. " + name + "입니다.")
