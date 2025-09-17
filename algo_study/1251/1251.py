"""
1251_하나로_D4
N개의 섬을 연결하는 교통 시스템 설계 프로젝트
모든 섬을 연결하는 것이 목표
반드시 두 섬을 선분으로 연결
교차된다 하더라도 물리적으로 연결되지 않음

모든 섬을 연결해야 함 - 간접적으로 연결되어도 됨

환경 부담금 정책
환경 부담 세율(E) * (해저터널 길이의 제곱(L^2))
만큼 지불해야 함

총 환경 부담금을 최소로 지불하며 N개의 모든 섬을 연결할 수 있는 교통 시스템 설계

입력
TC
N
각 섬의 X좌표
각 섬의 Y좌표
"""

# 이번엔 Prim 알고리즘 쓸거임
# 프림 알고리즘
# BFS처럼 하는거
# 일단 첫번째 노드를 힙에 넣고
# 힙이 빌 때까지 반복하면서
# 힙에서 팝 한 다음에
# 방문처리하고
# 연결된 곳들을 푸시
# 만약 이미 방문했다면 가지 않음
# 방문처리하는 1차원 리스트 만들어야 함
from heapq import heappush, heappop
# from math import sqrt

import sys
sys.stdin = open('re_sample_input.txt')


# 프림 알고리즘
def prim(start_node):
    MST = [0] * N  # N개의 섬에 방문했는지 여부 저장 0 : 방문X
    # 힙
    pq = []  # priority_queue
    result = 0  # 전체 가중치 합

    # 첫번째 노드 저장
    heappush(pq, (adj_matrix[start_node][start_node], start_node))  # (가중치, 시작 노드)

    while pq:  # 비기 전까지 반복함
        weight, now_node = heappop(pq)
        # print(MST)
        if MST[now_node] == 1:  # 이미 방문했다면
            # print(now_node, '이미 방문했음')
            continue

        # 방문 X
        MST[now_node] = 1  # 방문처리
        result += weight  # 가중치 더하기
        # print(now_node, '방문처리', '현재', weight, '가중치', result)
        for next_node in range(N):  # next_node에 노드 번호가 들어가야 함
            # 만약 MST[next_node]가 0이라면(아직 방문안했다면)
            if MST[next_node] == 0:
                # print('heappush', (adj_matrix[now_node][next_node], next_node))
                heappush(pq, (adj_matrix[now_node][next_node], next_node))
            # 방문했다면 굳이 넣을 필요 없음
        # print(pq)
    # print('result =', result)
    return result

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    x_arr = list(map(int, input().split()))
    y_arr = list(map(int, input().split()))
    E = float(input())
    # print(N, E)
    # 거리를 계산해서 모든 간선을 연결한 완전 그래프 만들어야 하니까
    # 인접 행렬 사용
    adj_matrix = [[0] * N for _ in range(N)]  # 섬은 0부터 N-1번까지 있음
    for n1 in range(N):
        for n2 in range(n1 + 1, N):
            weight = E * ((x_arr[n1] - x_arr[n2])**2 + (y_arr[n1] - y_arr[n2])**2)
            # 환경 부담 세율(E) * (해저터널 길이의 제곱(L^2))
            # 해저터널 길이 = sqrt((x1-x2)**2 + (y1-y2)**2)
            # 근데 어차피 환경 부담 세율 계산할 때 제곱 쓰기 때문에 sqrt 필요 없음
            adj_matrix[n1][n2] = weight
            adj_matrix[n2][n1] = weight

    # # 출력
    # for i in range(N):
    #     print(adj_matrix[i])

    # result = prim(0)
    # print(result)
    # print(int(result))
    result = int(round(prim(0),0))  # 어디서 시작하든 결과는 동일해야 함

    print(f'#{test_case} {result}')
