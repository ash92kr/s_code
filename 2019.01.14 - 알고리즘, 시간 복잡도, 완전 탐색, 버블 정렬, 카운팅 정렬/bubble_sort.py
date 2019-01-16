def bubblesort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]:   # 부등호의 방향을 바꾸면 오름/내름차순이 됨
                data[j], data[j+1] = data[j+1], data[j]

    return data

data = [41, 61, 20, 99, 37, 6]
# 함수를 통해서 리스트 원소를 바꾸면 값이 바뀐다(그냥 값을 주면 바뀌지 않음)
# 함수에게 리스트 원본(의 주소를) 주므로 함수를 통해 값을 바꾸면 리스트 원본의 값도 바뀐다(참조 타입)
print(bubblesort(data))



