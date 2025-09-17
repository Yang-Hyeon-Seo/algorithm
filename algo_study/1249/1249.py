"""
1249_보급로_D4
전쟁 - 전투 진행 지역은 도로 곳곳이 파손됨
도로들은 전투로 인해 트럭이나 탱크와 같은 차량이 지나갈 수 없음
출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대해 총 복구시간 구하기
노드 안의 숫자가 복구 시간임
복구 시간이 가장 짧은거... 특정 노드에 대해서 다익스트라?
"""

# 다익스트라
# 거리를 기록할 리스트 필요함
# 첫번째 노드부터 직접 연결된 노드들을 확인해서
# 이동 가중치가 기존에 있는 리스트보다 짧으면 갱신

# 가장 긴 대각선 기준으로 해서 출발지, 도착지에서 각 대각선까지 이동할 때 걸린 거리를 구하고
# 두개 쌍을 맞춰서 더하기
from heapq import heappush, heappop

def dijkstra(start_node):
    INF = float('inf')
    distances = [INF] * N  # 대각선에 있는 칸들은 N개가 있기 때문에

    pq = []

    # 첫번째 노드 넣기
    heappush(pq, (graph[start_node][start_node], start_node))
    # (가중치, 노드번호)

    while pq:  # pq가 채워져 있는 동안 반복
        weight, now_node = heappop(pq)
        print(weight, now_node, distances)
        if distances[now_node] > weight:
            # 갱신해야 함
            print('갱신')
            distances[now_node] += weight

            for next_node in range(N):
                heappush(pq, (graph[now_node][next_node], next_node))
            print(pq)
    return distances



import sys
sys.stdin = open('input.txt')

from collections import deque


# # DFS
# def dfs():
#     if

# # 델타로 완전탐색해서 풀고, 가지치기하면 풀 수 있을 것 같긴 함
# # 다익스트라 쓸 수 있을 것 같았는데 생각이 안남 / 가장 큰 대각선 기준으로 해보면 될 것 같기도 한데
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]  # 우, 하, 좌, 상

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, list(input()))) for _ in range(N)]

    for i in range(N):
        print(graph[i])

    # # [0][0]부터 시작할거임
    # stack = deque([(0, 0)])
    #
    # # 그냥 오른쪽 아니면 왼쪽으로 이동해서 G까지 도착했을 때 더 작은거 채택하면 되는 것 아님?
    # drc = [(0, 1), (1, 0)]  # (r, c) 오른쪽, 아래 순서
    #
    # while stack

    result = dijkstra(0)
    print(result)
    # print(f'#{test_case} {result[-1]}')

