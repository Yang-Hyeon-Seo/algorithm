import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M, X, K, target_N, target_M = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    customer = list(map(int, input().split()))

    que1 = deque()
    que2 = deque()

    # [[접수번호, 수리번호], [...], ...]의 형태로 저장할거임
    result = []

    # while True:
    #     # 고객의 정보가 정렬되어 들어오니까 일단 첫번째 고객 들어올 때까지 기다리기
    i = 0
    while i < len(customer):
        arrive_time = customer[i]

        j = i
        while j < len(customer) and arrive_time == customer[j]:  # 동시에 온 사람들 다 큐에 넣음
            que1.append(customer[j])
            j += 1

        # 큐에서 뽑아서 접수번호 주기

        # 큐2에 넣기

        # 큐2에서 뽑아서 수리 번호 주기

        # 남은 시간들 중에 가장 작은거 보고 하기 (음 큐를 쓰면 안될지도)

