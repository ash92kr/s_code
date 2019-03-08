import sys
sys.stdin = open("반나누기_input.txt")

def max_min(A, B, C):  # 조건문을 통해 최소/최대 인원 return

    global max_N, min_N

    if A >= B:
        if C >= A:
            max_N = C
            min_N = B
        else:
            if B >= C:
                max_N = A
                min_N = C
            else:
                max_N = A
                min_N = B
    else:
        if C >= B:
            max_N = C
            min_N = A
        else:
            if C >= A:
                max_N = B
                min_N = A
            else:
                max_N = B
                min_N = C

    return max_N, min_N


T = int(input())

for tc in range(T):

    N, K_min, K_max = map(int, input().split())   # N = 사원 수, K - 각 반에 배정되어야 하는 최소/최대 인원

    eng = list(map(int, input().split()))   # 각 사원의 영어 성적

    for i in range(len(eng)-1):   # 영어 성적 버블 정렬
        for j in range(i+1, len(eng)):
            if eng[i] > eng[j]:
                eng[i], eng[j] = eng[j], eng[i]

    min_eng = eng[0]   # 반을 가르는 영어 성적 기준 범위
    max_eng = eng[-1]

    sol = 9999   # 최대 배정 인원 - 최소 배정 인원의 최솟값을 구할 변수
    count = 0   # 카운트 변수

    for i in range(min_eng, max_eng):  # i는 최소 점수에서 최대 점수 -1까지
        for j in range(i+1, max_eng+1):   # j는 i+1점부터 최대 점수까지 반복
            A = 0   # 각 반에 속하는 인원 초기화(이 부분 헷갈림)
            B = 0
            C = 0
            for k in range(len(eng)):   # 기준 2개가 설정되고 난 다음 인원 배정
                if eng[k] < i:
                    C += 1
                elif i <= eng[k] < j:
                    B += 1
                else:
                    A += 1
            max_N = 0   # 세 반 중 최대 인원
            min_N = 0   # 세 반 중 최소 인원
            if K_min <= A <= K_max and K_min <= B <= K_max and K_min <= C <= K_max:   # 모든 반이 최소 ~ 최대 인원 사이에 있으면
                count += 1   # 카운트 변수 추가
                max_min(A, B, C)   # 각 반 중 최소/최대 인원 구하기
                if sol > max_N - min_N:   # 최대 인원 - 최소 인원의 최솟값을 구하기
                    sol = max_N - min_N

    if count == 0:   # 단 한 번도 최소/최대 인원을 만족하지 못하면 -1 출력
        print(-1)
    else:
        print(sol)
