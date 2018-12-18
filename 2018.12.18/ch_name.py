import os

os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
# 우리가 가야할 곳의 폴더 주소를 알려주어야 한다

# for filename in os.listdir("."):   # 우리가 현재 있는 폴더 위치 = .
#     os.rename(filename, "SAMSUNG " + filename)   # filename = 현재 파일 이름

# samsung 대신 saffy를 넣어야 한다
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG", "SAFFY"))
    

