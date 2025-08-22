"""
첫 줄에는 트리 정점의 총 수 V가 주어짐
다음 줄에는 V - 1개의 간선이 나열됨간선은 그것을 이루는 두 정점으로 표기됨
간선은 항상 부모 자식 순서로 표기됨

전위 중위 후위 모두 구현
"""
import sys
sys.stdin = open('input.txt')


# 전위
def preorder_traversal(n, left, right):
    """
    순회를 시작할 위치 n부터 시작해서
    n 방문(프린트), 왼쪽 , 오른쪽 순서대로 순회하는 코드 작성
    """
    if n != 0:  # 이 조건문이 중요함 -> 0이라는 조건을 넣지 않으면 무한루프에 빠짐
        print(n, end=' ')
        preorder_traversal(left[n], left, right)  # n이 부모 노드니까 인덱스로 사용
        preorder_traversal(right[n], left, right)
    return None


# 중위
def inorder_traversal(n, left, right):
    """
    순회를 시작할 위치 n에서 부터 시작
    왼쪽 갔다가 현재 위치 확인하고 오른쪽으로 감
    """
    if n != 0:  # n이 0이 아니어야 함(0이면 0번째 인덱스 접근하면서 이상해짐)
        inorder_traversal(left[n], left, right)
        print(n, end=' ')
        inorder_traversal(right[n], left, right)


# 후위
def postorder_traversal(n, left, right):
    """
    왼쪽 갔다가 오른쪽 갔다가 현재 위치 확인함
    """
    if n != 0:
        postorder_traversal(left[n], left, right)
        postorder_traversal(right[n], left, right)
        print(n, end= ' ')


# 입력
V = int(input())  # 정점의 수
E = V - 1  # 간선의 수

left = [0] * (V+1)
right = [0] * (V+1)

edge = list(map(int, input().split()))  # 간선 입력

for i in range(E):
    parent, child = edge[i*2], edge[i*2+1]

    if left[parent] == 0:  # 0이면 아직 값이 저장되지 않은 것임
        left[parent] = child
    else:  # 이미 left에 값이 채워짐
        right[parent] = child

# print(edge)
# print(left)
# print(right)

print('전위순회')
preorder_traversal(1, left, right)  # 1번 노드부터 순회

print('\n중위순회')
inorder_traversal(1, left, right)  # 1번 노드부터 순회

print('\n후위순회')
postorder_traversal(1, left, right)  # 1번 노드부터 순회
