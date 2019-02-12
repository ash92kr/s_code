
# problem 06

# def up_and_low(words):
#
#     new_word = ""
#
#     for i in range(len(words)):
#         if i % 2 == 0:
#             new_word += words[i].upper()
#         else:
#             new_word += words[i].lower()
#
#     return new_word
#
# print(up_and_low('applepie'))
# print(up_and_low('spaceship'))


# def pattern(n):
#
#     pattern = ""
#
#     if n < 1:
#         return ""
#     elif n % 2 == 1:
#         for i in range(n):
#             if (i+1) % 2 == 1
#                 pattern += str(i+1) * (i+1)

# import operator

# def passpass(test):
#
#     over_60 = {}
#
#     for key, value in test.items():
#         if value >= 60:
#             over_60.update({key: value})
#
#     # over_60 = sorted(over_60.items(), key=operator.itemgetter(0))
#
#     # over_60 = sorted(over_60)
#
#     for key in sorted(over_60):
#         over_60.update({key: over_60[key]})
#
#     return over_60
#
# print(passpass({"Java": 10, "Ruby": 80, "Python": 65}))


# def create_dict(keys, values):
#
#     make = {}
#
#     if len(keys) > len(values):
#         for i in range(len(keys)-len(values)):
#             values.append(None)
#     elif len(values) > len(keys):
#         for i in range(len(keys)-len(values)):
#             values.pop()
#
#     for i in range(len(keys)):
#         make.update({keys[i] : values[i]})
#
#     return make
#
# print(create_dict(['a', 'b', 'c', 'd'], [1, 2, 3]))
# print(create_dict(['a', 'b', 'c'], [1, 2, 3, 4]))


# problem 06-2
# def add(*args):
#
#     plus = 0
#
#     if len(args) == 0:
#         return 0
#
#     for i in range(len(args)):
#         plus += (args[i] * (i+1))
#
#     return plus
#
# print(add(3, 4, 5, 6, 7))
# print(add(2, 5, 5, 7, 7))
# print(add(0, 4, -1, 2, 1))


# slide 09

# class Stack:
#
#     def __init__(self):
#         # self.stack = []    # 생성자도 self를 넣어주어야 한다
#
#     def empty(self):
#         if not self.stack:
#             return True
#         else:
#             return False
#
#     def top(self):
#         return self.stack[-1]
#
#     def pop(self):
#         return self.stack.pop()
#
#     def push(self, data):
#         self.stack.append(data)


# class Person:
#     count = 0
#
#     def __init__(self, name, age):
#         Person.count += 1
#         self.name = name
#         self.age = age
#
#     def greeting(self):
#         print(f'{self.name}입니다. 반가워요!')
#
#     def __add__(self, other):
#         print(f'나이 합은 {self.age + other.age}입니다.')
#
#     def __sub__(self, other):
#         print(f'나이 합은 {self.age - other.age}입니다.')


# homework
# class Person:
# 
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
# 
#     def greeting(self):
#         return f'안녕하세요. {self.name}입니다. {self.age}살입니다.'
#         return 자체에 넣는 것도 존재
# 
# p1 = Person('홍길동', 20)
# p2 = Person('둘리')

# print(p1.greeting())
# print(p1.greeting()) 
# print(p2.greeting())
# 메소드 부르는 방법 다시 복습


# workshop
# class Circle:
#
#     pi = 3.14
#
#     def __init__(self, r, x=0, y=0):
#         self.r = r
#         self.x = x
#         self.y = y
#
#     def area(self):
#         return self.r * self.r * Circle.pi
#
#     def circumference(self):
#         return 2 * Circle.pi * self.r
#
#     def center(self):
#         return (self.x, self.y)
#
#     def move(self, x, y):
#         self.x = x
#         self.y = y
#         return f'({self.x},{self.y})로 이동되었습니다.'

        # return self.center()


#
# c1 = Circle(3)
# print(c1.center())
# print(c1.move(3, 3))
# print(c1.circumference())
# print(c1.area())
#
# c2 = Circle(1, 5, 5)
# print(c2.center())
# print(c2.circumference())
# print(c2.area())






# class Circle:
#     def __init__(self, center, r):
#         self.center = center
#         self.r = r
#
# # 인스턴스 변수 | 타입
# # center | point 클래스 인스턴스
#
# p1 = Point(0, 0)



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, center, r):
        self.x = center.x
        self.y = center.y
        self.r = r

    def get_area(self):
        return 3.14 * (self.r ** 2)

    def get_perimeter(self):
        return 3.14 * 2 * self.r

    def get_center(self):
        return (self.x, self.y)

    def print(self):
        print(f'Circle: ({self.x}, {self.y}), r: {self.r}')


p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()

p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()

