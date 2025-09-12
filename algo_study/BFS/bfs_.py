"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

N, E = map(int, input().split())
# 이번엔 인접 행렬로 만들어 보기
adj_matrix = [[0] * (N+1) for _ in range(N+1)]  # 0번 인덱스는 사용 X
input_arr = list(map(int, input().split()))

for i in range(E):
    adj_matrix[input_arr[2 * i]][input_arr[2 * i + 1]] = 1
    adj_matrix[input_arr[2 * i + 1]][input_arr[2 * i]] = 1

for i in range(N):
    print(adj_matrix[i])


def bfs(current_node, visited, path):
    que = [current_node]
    while que:
        node = que.pop(0)
        if visited[node] is not True:
            visited[node] = True
            path.append(node)
        for i in range(1, N+1):
            if adj_matrix[node][i] == 1 and visited[i] is not True:
                que.append(i)
        print(que)


visited = [False] * (N+1)
path = []
bfs(1, visited, path)
print(*path)