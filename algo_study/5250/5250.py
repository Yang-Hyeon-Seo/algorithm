"""
5250_최소비용_D3
출발지에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라짐
최적의 경로로 이동하면 최소한의 연료로 이동 가능
출발은 왼쪽 위, 도착은 가장 아래
각 칸에서는 상하좌우 칸이 나타내는 인접지역으로만 이동 가능
이동 시 기본적으로 1만큼 연료가 더 들고
더 높은 곳으로 이동하는 경우에는 높이 차이만큼 연료가 추가로 듦

최소 연료 소비량을 출력하는 프로그램
"""
from collections import deque

# 다익스트라인데 이중 배열로
def dijkstra_2d(N):
    # 필요한 것들 만들기
    distances = [[0] * N for _ in range(N)]
    q = deque()


    # 초기화(무조건 왼쪽 위부터 시작)
    for r in range(N):
        for c in range(N):
            if r == 0 and c == 0:
                # 첫번째 칸은 스킵
                continue
            if c - 1 >= 0:
                weight = distances[r][c - 1] + 1 + max(adj_matrix[r][c] - adj_matrix[r][c - 1], 0)
                if distances[r][c] == 0:
                    # 갱신된적 없음
                    distances[r][c] = weight
                else:
                    distances[r][c] = min(distances[r][c], weight)  # 둘 중에 작은거
            if r - 1 >= 0:
                weight = distances[r - 1][c] + 1 + max(adj_matrix[r][c] - adj_matrix[r - 1][c], 0)
                if distances[r][c] == 0:
                    # 갱신된적 없음
                    distances[r][c] = weight
                else:
                    distances[r][c] = min(distances[r][c], weight)  # 둘 중에 작은거

    # for i in range(N):
    #     print(distances[i])

    return distances


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    adj_matrix = [list(map(int, input().split())) for _ in range(N)]

    # 이중 리스트로 위치 정보들 저장하면서 만들어보자
    dij_list = dijkstra_2d(N)

    print(f'#{test_case} {dij_list[-1][-1]}')