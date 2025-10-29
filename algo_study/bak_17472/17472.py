"""
백준 17472번

"""

# import sys
# sys.stdin = open('input.txt')

# 백준 입력
import sys

dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dc = [0, 1, 0, -1]


def find_island(arr, r, c, number_of_island):
    """
    1-1
    섬 번호 매기는 함수
    """
    arr[r][c] = number_of_island  # 섬 번호 갱신
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
            # 벽 안에 있고, 해당 위치의 숫자가 1이라면
            find_island(arr, nr, nc, number_of_island)
            # 재귀적으로 자기자신을 호출함


def find_min_distance(arr, island, graph):
    # min_distance = float('inf')
    for r in range(N):
        for c in range(M):
            if arr[r][c] == island:  # 섬 번호와 같으면
                for i in range(4):  # 4 방향을 확인하면서
                    # print(r, c, arr[r][c], '방향', i, '확인')
                    nr = r + dr[i]
                    nc = c + dc[i]
                    distance = 0
                    # count 변수는 실제로 사용하지 않았는데, if문 수정 안 하려고 그냥 둠
                    count = True  # 카운트 하거나 안 하거나 결정하는 변수
                    # 벽체크 겹치는거 해결할 수 있지 않을까 싶은데 모르겠음
                    # print(nr, nc, distance)
                    while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0: # 벽 안에 있거나 해당 값이 0일 때까지 반복하기
                        distance += 1
                        # print(nr, nc, distance)
                        # 다음 위치 이동
                        nr = nr + dr[i]
                        nc = nc + dc[i]

                    if 0 > nr or nr >= N or 0 > nc or nc >= M:
                        # 벽 뚫어서 while이 끝났다면 해당 거리는 count하지 않음
                        count = False  # 카운트하지 않음
                    else:
                        # 벽 뚫어서 while이 끝난게 아니라면
                        if distance > 1 and graph[arr[nr][nc]][arr[r][c]] > distance:
                            graph[arr[nr][nc]][arr[r][c]] = distance
                            graph[arr[r][c]][arr[nr][nc]] = distance  # 양방향
                            # 그래프에 추가하기


def make_set(number_of_island):  # 0부터 number_of_island-1만큼 길이인데, 0이랑 1은 안 쓸거임
    arr = []
    for n in range(number_of_island):
        arr.append(n)
    return arr

def find_boss(a, arr):  # 서로소 대표 찾기
    if a == arr[a]:
        return arr[a]  # 자기자신이랑 같으면 자기자신 반환
    new_boss = find_boss(arr[a], arr)  # 새로운 보스를 찾아 반환하기
    return new_boss  # 아니면 보스 다시 찾음
    # 돌면서 가중치 가장 작은것들 연결
def union_ab(a, b, arr):
    a_boss = find_boss(a, arr)
    b_boss = find_boss(b, arr)
    if a_boss > b_boss:  # 더 큰쪽으로 합치기
        arr[b] = a_boss
    else:
        arr[a] = b_boss


# T = int(input().strip())
# for test_case in range(1, T+1):
N, M = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

line = sys.stdin

# 1단계 : 1, 2, 3, 4, ... 각 섬에서 다른 섬까지 가는 거리를 구해서
# 인접 리스트로 만든다

# 1-1
# 1인 곳을 찾아서 델타로 연결된 섬을 새로 지정
# 섬 번호는 2부터 시작
number_of_island = 2
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            # 1인 경우에
            find_island(arr, r, c, number_of_island)
            # 함수가 끝나면
            number_of_island += 1  # 섬 번호 1 늘리기

# max_island = number_of_island - 1
# for i in range(N):
#     print(arr[i])

# 1-2
# 각 섬에서 다른 섬으로 연결하는 최소 거리(단, 2 이상)을 구한다
graph = [[float('inf')] * number_of_island for _ in range(number_of_island)]  # 0, 1번 인덱스는 사용하지 않음
for island in range(2, number_of_island):
    find_min_distance(arr, island, graph)

# for i in range(2, number_of_island):
#     print(graph[i][2:])

# 연결 형태를(가중치, 시작, 끝) 이렇게 해서 리스트로 만들어야 함
graph_tuple = []
for i in range(2, number_of_island):
    for j in range(i, number_of_island):
        if graph[i][j] < float('inf'):
            # 거리가 있다면
            graph_tuple.append((graph[i][j], i, j))

# print(graph_tuple)

graph_tuple.sort() # 오름차순 정렬

# 서로소 집합 만들기
linked_set = make_set(number_of_island)

total_length = 0

for i in range(len(graph_tuple)):  # graph_tuple만큼 반복
    w, a, b = graph_tuple[i]  # 거리, 시작섬, 끝섬
    # a, b 연결하고 w 더하기
    if find_boss(a, linked_set) != find_boss(b, linked_set):  # a와 b의 집합이 다르다면
        union_ab(a, b, linked_set)  # a와 b를 합친다
        total_length += w  # 거리를 더한다
        # print(a, b, total_length, linked_set)

if total_length == 0:
    total_length = -1
# print(linked_set)  # 결과 서로소 확인하기
print(total_length)

# 크루스칼 or 프림 알고리즘 이용해서 모든 섬 연결하는 최소 비용 구하기
# 크루스칼
# 일단 각 섬에서 가는 길이랑 연결될 섬을 저장

# 프림 - heap 이용하기


#
# 크루스칼
# 일단 서로소 집합 만들어서 서로소집합에서 진행할 것들 함수로 만듦
