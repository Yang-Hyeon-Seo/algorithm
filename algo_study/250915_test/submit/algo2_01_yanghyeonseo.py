"""
사과문제
최소 거리 - BFS
"""

# import sys
# sys.stdin = open('algo2_sample_in.txt')


def DFS(start, visited, count):
    # 방문처리
    visited[start] = True
    # print('방문처리', count)

    for i in range(N+1):
        if visited[i] is not True:
            # 방문하지 않았을 떄
            # print(i, '방문')
            DFS(i, visited, count + adj_matirx[start][i])

    visited[start] = False
    # print('방문처리 취소')
    # 순열 구하기



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    apples = [list(map(int, input().split())) for _ in range(N)]
    # print(apples)
# abs 함수
    # 인접 행렬 만들기
    adj_matirx = [[0] * (N+1) for _ in range(N+1)]  # 0번 인덱스는 창고
    # 각 정점에서 거리 구하기
    apples = [[0, 0]] + apples  # 창고 인덱스 추가하기
    # print(apples)
    for i in range(N+1):
        for j in range(i+1, N+1):
            # print(i, j)
            d = abs(apples[i][0] - apples[j][0]) + abs(apples[i][1] - apples[j][1])
            adj_matirx[i][j], adj_matirx[j][i] = d, d

    # 인접행렬 출력
    # for i in range(len(adj_matirx)):
    #     print(adj_matirx[i])


    # DFS 형식으로 거리 계산하기
    visited = [False] * (N+1)

    DFS(0, visited, 0)
