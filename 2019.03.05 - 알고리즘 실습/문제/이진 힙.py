import sys
sys.stdin = open("이진 힙_input.txt")

def make_heap(node):

    global last, heap

    last += 1   # 삽입 시에는 가장 마지막에 삽입한다
    child = last   # 자식 노드와 부모 노드 설정
    parent = child // 2
    heap[last] = node

    while child > 1 and heap[parent] > heap[child]:   # 부모 노드의 값이 자식 노드의 값보다 크면
        heap[parent], heap[child] = heap[child], heap[parent]   # 값 교체
        child = parent  # 자식은 부모의 인덱스로 교체
        parent = parent // 2  # 자식은 왼쪽과 오른쪽이 있으므로 부모 인덱스는 2로 나눈 몫


def sum_heap(node):

    hap = 0

    while node >= 1:   # 현재 노드에서 루트 노드까지 원소의 합을 더한다
        node = node // 2
        hap += heap[node]

    return hap

T = int(input())

for tc in range(T):

    N = int(input())
    data = list(map(int, input().split()))

    heap = [0] * (N+1)   # 힙도 이진 트리의 특수한 경우이므로 N+1개의 배열을 만듦
    last = 0

    for i in range(N):
        make_heap(data[i])

    # print(heap)

    print("#{} {}".format(tc+1, sum_heap(N)))

