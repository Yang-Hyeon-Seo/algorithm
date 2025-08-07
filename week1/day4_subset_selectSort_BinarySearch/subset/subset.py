'''
10개의 정수를 받아 부분집합의 합이 0이 되는 것이 존재하는지 계산하는 함수 작성
'''

# 함수 생성
def is_subset_zero(arr):
    '''
    10개의 정수를 받아 부분집합의 합이 0이 되는 것이 존재하는지 계산
    '''
    # arr의 길이 받기
    N = len(arr)
    # 부분집합 찾기(비트 활용)
    for i in range(1<<N): # 2ⁿ번 반복 # 공집합 계산 안 하려면 range(1, 1<<N) 이렇게 하면 됨
        # 부분집합 원소 저장
        subset = []     # 이렇게 subset으로 안 하고
        # result = 0
        for j in range(N): # 확인할 자리만큼 반복
            if i & (1<<j): # 2^j 자리에 값이 있는지 확인 (j번째 요소가 있는지 확인)
                subset.append(arr[j])
                # result += arr[j]
        if len(subset) > 0 and sum(subset) == 0: # 공집합 이외에 합이 0이 되는 subset이 있는지 확인
        # if len(subset) > 0 and result: #이렇게 할 수도 있을 듯
            return 1 # 있음
    return 0 # 없음
# input 입력
import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{test_case} {is_subset_zero(arr)}')