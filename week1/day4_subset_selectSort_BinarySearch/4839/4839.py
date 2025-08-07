'''
이진탐색
A, B 두 사람에게 교과서에서 각자 찾을 쪽을 주면,
이진탐색만으로 지정된 페이지를 먼저 편치는 사람이 이기는 게임
왼쪽 : l
오른쪽 : r
중간 : c
'''
# 재귀함수 이용해보기 - 이유 : 재귀함수는 잘 안쓰게 되니까
def binary_search(l, r, key):
    c = (l + r) // 2
    if key == c:
        return 1 # search 1번 수행
    elif key > c: # key가 더 큰 경우, 오른쪽에서 탐색
        return binary_search(c, r, key) + 1
    else: # key가 더 작은 경우
        return binary_search(l, c, key) + 1

# 입력
import sys
sys.stdin = open('sample_input.txt')
T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    # 순서대로 total_page, A_page, B_page 의미
    A = binary_search(1, P, Pa) # A가 찾는데 걸린 연산
    B = binary_search(1, P, Pb) # B가 찾는데 걸린 연산
    #print(A, B)
    if A > B:     #A가 더 오래 걸린 경우 -> B가 이김
        print(f'#{test_case} B')
    elif A == B : #비기는 경우
        print(f'#{test_case} 0')
    else: # A < B # B가 더 오래 걸리는 경우 -> A가 이김
        print(f'#{test_case} A')