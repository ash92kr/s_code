def func():
    print("function A.py")

print(f"A의 __name__은 {__name__}.")
print('top-level A.py')

if __name__ == "__main__":  # 모듈의 이름이 저장되는 __main__ 메소드
    print('A.py가 직접 실행한 경우')  # 직접 import
else:
    print('B.py가 import되어 사용된 경우')