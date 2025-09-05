"""
4837_부분집합의 합
1부터 12까지 숫자를 원소로 가진 집합 A가 있음
집합 A의 부분집합 중 N개 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램 작성

"""

import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, T+1):
    N, K = map(int, input().split())  # N : 부분집합 원소의 수, 부분집합의 합 K
    # 1부터 12까지의 숫자를 원소로 가진 집합 -> 2의 12제곱 만큼의 경우의 수 존재
    # 이 중에 5개만 가지고 있어야 함