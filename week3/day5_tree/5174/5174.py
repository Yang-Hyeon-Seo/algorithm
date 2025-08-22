"""
트리의 일부를 서브트리라고 함
주어진 이진트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램 만들기

"""

# 아이디어
"""
순회하면서 순회할 때마다 count + 1하면 그 안에 포함된 노드의 개수 알 수 있을 것 같음
"""

import sys
sys.stdin = open("sample_input.txt")


# 순회하면서 count하는 함수
def count_node(node, left, right):
    """
    순회하면서 n이 0이 아니면(탐색할 대상이면 count + 1)
    preorder_traversal 느낌으로
    """
    if node != 0:
        count_left = count_node(left[node], left, right)
        count_right = count_node(right[node], left, right)
        # print(node, count_left, count_right, count_right + count_left + 1)
        return count_right + count_left + 1
    else:
        return 0



T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1

    left = [0] * (V+1)
    right = [0] * (V+1)

    edge = list(map(int, input().split()))

    for i in range(E):
        parent, child = edge[i*2], edge[i*2+1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    result = count_node(N, left, right)
    print(f'#{test_case} {result}')
