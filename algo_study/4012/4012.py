"""
4012_요리사
두명의 손님에게 음식 제공
식성이 비슷해서 최대한 비슷한 맛의 음식 만들어야 함
N개의 식잴가 있음
식재료를 N/2로 나눠서 2개의 요리를 해야 함

비슷한 맛의 음식을 만들기 위해서는 A와 B의 맛 차이가 최소가 되도록 재료 배분해야 함

식재료 i는 식재료 j와 궁합이 잘맞아 시너지 Sij가 발생함
각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지의 합임

식재료 i를 j와 같이 요리하게 되면 발생하는 시너지 Sij정보가 주어짐
가지고 있는 식재료를 이용해 A와 B를 만들 때 두 음식 간 차이가 최소가 되는 경우 찾고
그 최소값을 출력하는 프로그램

"""
from itertools import combinations

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')
    for i in range(N):
        print(arr[i])

    # 2개 고르는 조합
    # for i in range(N):
    #     for j in range(i+1, N):
    #         A = arr[i][j] + arr[j][i]
    #
    #         for m in range(N):
    #             for n in range(m+1, N):
    #                 if m == i or m == j or n == i or n == j:
    #                     continue
    #                 B = arr[m][n] + arr[n][m]
    #                 print(i, j, A, ' / ', m, n, B)
    #                 if abs(A-B) < min_diff:
    #                     print(abs(A-B) , min_diff)
    #                     min_diff = abs(A-B)

    # 이게 아니고 N/2만큼 쪼개는 거임
    comb = combinations([i for i in range(N)], int(N/2))
    for i in comb:
        print(i)
    print(f'#{test_case} {min_diff}')