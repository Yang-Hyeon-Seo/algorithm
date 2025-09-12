"""
4835_구간합_D2
N개의 정수가 들어있는 배열
이웃한 M개의 합을 계산
가장 큰 경우와 가장 작은 경우의 차이 출력
"""

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_count = 0
    min_count = 100*10000+1  # 불가능한 수

    for i in range(N-M+1):
        count = 0
        for j in range(M):
            count += arr[i+j]
        if count > max_count:
            max_count = count
        if count < min_count:
            min_count = count
        # print(count, max_count, min_count)

    print(f'#{test_case} {max_count - min_count}')