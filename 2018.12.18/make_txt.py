# f = open("new.txt", "w")   # 파일을 만들면서 열기
# f.write("Hello World")    # 파일에 쓰는 내용
# f.close()    # 저장하면서 닫기

# with open("new.txt", "w") as f:
#     f.write("hungry데스")   # a로 쓰면 원래 내용이 없어지지 않고 추가됨

# f = open("new.txt", "r")   # 파일의 모든 내용 읽어오기
# data = f.read()   # 파일 읽기
# print(data)
# f.close()

# with open("new.txt", "r") as f :
#     data = f.read()
#     print(data)

# f = open("new.txt", "w", encoding='utf-8')   # 파일을 한번 연다
# for i in range(0,6):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
# f.close()   # 파일을 여러 번 닫으면 에러 발생

# with open("new.txt", "w", encoding='utf-8') as f :
#     for i in range(0, 10):
#         data = f'{i}번째 줄입니다.\n'
#         f.write(data)


menu = ["제육볶음 ", "카레라이스 ", "볶음우동 ", "탕수육"]
# f = open("menu.txt", "w", encoding='utf-8')
# f.writelines(menu)
# f.close()

with open("menu.txt", "w", encoding='utf-8') as f:
    f.writelines(menu)




# with open("tap.txt", "w", encoding="utf-8") as f:
#     for i in range(6):
#         data = f'점심시간까지 {6-i}분 남았습니다.\t'
#         f.write(data)


f = open("tap.txt", "w", encoding="utf-8")
for i in range(0, 10):
    data = f'점심시간까지 {10-i}분 남았습니다.\t'
    f.write(data)
f.close()







