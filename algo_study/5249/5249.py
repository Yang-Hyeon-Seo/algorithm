"""
5249_최소신장트리_D4
0부터 V까지의 노드
E개의 간선
최소 신장 트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램
"""

# kruskal 알고리즘
import sys
sys.stdin = open('sample_input.txt')


# 서로소 함수
def find_parents(x, parents):
    if x == parents[x]:
        return x
    parents[x] = find_parents(parents[x], parents)
    return parents[x]


def union(x, y, parents):
    rx = find_parents(x, parents)
    ry = find_parents(y, parents)

    if rx == ry:
        # 같은 집합
        return
    if rx > ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

# krusal 알고리즘 - 함수
def krusal():
    cnt = 0  # 연결한 간선의 수
    result = 0  # 연결한 간선의 가중치

    # 1. 간선들 정보를 저장한 리스트 만듦
    edges = []
    for i in range(E):
        start, end, weight = map(int, input().split())
        edges.append((weight, start, end))

    # 2. 간선들 정보를 오름차순으로 정렬
    edges.sort()

    # print(edges)

    parents = [i for i in range(V + 1)]
    # 3. 간선 가중치가 작은 것들부터 하나씩 선택
    for weight, start, end in edges:
        # 서로소 집합 만들기

        # print(parents)
        # print(start, end, end=' / ')

        #   3-1. 만약 사이클이 만들어진다면(같은 서로소집합이라면) continue
        if find_parents(start, parents) == find_parents(end, parents):
            # 사이클이 만들어짐

            # print(find_parents(start, parents), find_parents(end, parents), '사이클')

            continue

    #   3-2. 사이클이 만들어지지 않는다면 추가
        # 사이클이 안 만들어짐
        union(start, end, parents)
        cnt += 1
        result += weight

        # print(f'사이클x / cnt = {cnt} / result = {result}')

        if cnt == V:  # 0부터 V까지 총 V+1개의 노드가 있으니까 간선은 V개
            break

    return result

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]  # 0번부터 V번까지 노드
    # print(graph)

    result = krusal()

    print(f'#{test_case} {result}')
    # for _ in range(E):
    #     start, end, weight = map(int, input().split())
    #     graph[start].append((weight, end))
    #     graph[end].append((weight, start))

    # print(graph)