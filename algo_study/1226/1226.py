"""
1226_미로_D4
16x16 행렬 형태의 미로에서 2에서 출발해서 0만 지나서 3으로 가는 길 찾기
도착 가능하면 1, 불가능하면 0
다익스트라 이용하는데
중간에 그만두기
"""

import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush

dr = [0, 1, 0, -1]  # 오 아 왼 위
dc = [1, 0, -1, 0]

def dijkstra(graph, start):
    INF = float('inf')
    distances = [[INF] * 16 for _ in range(16)]
    pq = []

    distances[start[0]][start[1]] = 0
    heappush(pq, (0, (start[0], start[1])))

    while pq:
        now_weight, now_pos_r, now_pos_c = heappop(pq)

        if now_weight > distances[now_pos_r][now_pos_c]:
            continue








# 근데 BFS로 해도 될듯



T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, list(input()))) for _ in range(16)]


    for i in range(16):
        print(arr[i])