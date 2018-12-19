
# 출력될 값은?

if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")


# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램 작성하기

item = int(input("번호를 입력하세요."))   # str이 되므로 int로 캐스팅해야 한다

if item > 0:
    for i in range(item):
        i += 1   # 0부터 출력되기 때문에 i+1을 해줘야 한다
        print(i)


'''
투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력받고 해당 종목이 투자 경고 종목이라면
'투자 경고 종목입니다.'를, 아니면 '투자 경고 종목이 아닙니다.'라고 출력하기
'''

warn_investment_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
print(f'경고 종목 리스트: {warn_investment_list}')
item = input('투자종목이 무엇입니까?: ')

item2 = item.lower()

if item2 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")



'''
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
다음 리스트에서 0, 4, 5번째 요소를 지운 새로운 리스트를 생성하시오.
'''

colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

# colors2 = ['Banana', 'Coconut', 'Deli']

colors2=[]

for i in range(len(colors)):
    if i in [0, 4, 5]:
        pass
    else:
        colors2.append(colors[i])

print(colors2)

# colors2 = []
# colors.remove('Apple', 'Ele', 'Grape')


# deleteindex = [0, 4, 5]

# fruit = []
# for i in range(0, len(colors)):
#     if i not in deleteindex:
#         fruit.append(colors[i])
# print(fruit)


'''
ssafy의 semester1의 기간 출력
ssafy dictionary 안에 있는 대전 출력
daejeon의 매니저 이름 출력
'''

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}


print(ssafy['duration']['semester1'])
print(ssafy['location'][1])
print(ssafy['classes']['daejeon']['manager'])

