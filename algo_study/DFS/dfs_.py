# 입력
"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

N, E = map(int, input().split())  # 간선의 수, 노드의 수
arr = [[] for _ in range(N+1)]  # 0번 인덱스는 사용하지 않음
input_arr = list(map(int, input().split()))
for i in range(E):
    arr[input_arr[2*i]].append(input_arr[2*i + 1])
    arr[input_arr[2*i + 1]].append(input_arr[2*i])
print(arr)

def dfs(start, arr, visited, path):
    # 깊이 우선 탐색
    # 현재 노드가 이미 방문했다면 나감
    if visited[start] == True:
        return

    # 일단 방문 처리
    visited[start] = True
    # print(visited)
    path.append(start)
    # print(start, end="")

    for i in arr[start]:

        # 연결된 노드 방문
        dfs(i, arr, visited, path)
    # visited[start] = False

visited = [False] * (N+1)  # 노드 개수 + 1개, 0번 인덱스 이용 X
path = []
dfs(1, arr, visited, path)
print(*path)