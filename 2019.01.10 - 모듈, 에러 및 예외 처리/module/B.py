import A   # 파일 확장자는 입력할 필요 없음

print("top-level B.py")

A.func()   # A의 함수를 호출함

if __name__ == "__main__":
    print("B.py가 직접 실행된 경우 = main")
else:
    print("B.py가 import 되어 실행된 경우")