'''
버스는 0번에서 출발해 종점인 N번 정류장까지 이동
한 번 충전으로 최대한 이동할 수 있는 정류장 수 K
충전기가 설치된 M개의 정류장 번호가 주어질 때
최소한 몇 번 충전을 해야 종점에 도착할 수 있을지
충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 0 출력
출발지에는 항상 설치되어 있지만, 충전 횟수에는 포함하지X
'''

# 입력 받기
import sys

sys.stdin = open('sample_input.txt')

# 테스트 케이스
T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    # M개의 정류장 번호
    stop_num = list(map(int, input().split()))
    # 충전 횟수
    charge_num = 0

    # counting sort처럼 리스트 만들기
    # 1 : 충전기가 있음
    # 0 : 충전기 없음
    # routine = [0] * (N+1)
    routine = [0] * (N)+ [2] * (K+1) # 연산을 간단하게 하기 위해 K만큼 더함 / N번 이후는 도착지 이후라서 2로 표현

    for i in stop_num:
        routine[i] = 1
    #print(routine)

    max_idx = 0 # 목적지 나타낼 것

    # 0부터 반복문을 돌면서 끝까지 갔을 때 charge_num이 몇이 되는지 확인
    for i in range(N+1): # i는 현재 위치
    # k 안에 충전기가 2개 이상 --> 제일 뒤에 있는 충전기까지 가면 됨(텔레포트), charge_num += 1
    # k 안에 충전기가 1개 --> 그 충전기로 가면 됨, charge_num += 1
    # k 안에 충전기가 없음 --> 0 출력
        # 만약 목적지 인덱스보다 작으면
        if i < max_idx:
            continue # 스킵

        if 2 in routine[i+1:i+K+1]: # 도착지까지 갈 수 있으면
            break

        elif 1 in routine[i+1:i+K+1]:
            # k 안에 충전기가 존재
            for j in range(1, K+1): # routine[i:i+K+1]: # 가장 멀리 있는 충전기의 인덱스 가리킴
                if routine[i+j] == 1:
                    max_idx = i+j

            charge_num += 1
        else: # k 안에 충전기 없음
            charge_num = 0
            break
    print(f'#{test_case} {charge_num}')