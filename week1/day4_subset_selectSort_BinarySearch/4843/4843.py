'''
N개의 정수가 주어지면
가장 큰수, 가장 작은수, 2번째 큰 수, 2번째 작은 수, ...
테스트케이스
정수의 개수
N개의 정수
'''

# 입력
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 큰 수 먼저 -> 작은수
    for i in range(N): #N만큼 반복
        # i가 짝수면 큰 수
        if i % 2 == 0: # 0이면
            max_idx = i
            for j in range(i+1, N): # 큰 수 찾기
                if arr[j] > arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i] # 자리 바꾸기
        # i가 홀수면 작은 수
        else:
            min_idx = i
            for j in range(i+1, N): # 작은 수 찾기
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i] # 자리 바꾸기
    print(f'#{test_case}', end = ' ')
    for i in range(10):
        print(arr[i], end = ' ')
    print()