"""
16811_당근포장하기_D2
N개의 당근을 주문하면 대, 중, 소 상자로 구분해 보장함
- 같은 크기의 당근은 같은 상자에 들어감
- 비어있는 상자 X
- 한 상자에 N//2개를 초과하는 당근이 있어서도 안됨
위 조건을 만족하면서도 당근의 개수가 차이가 최소가 되도록 포장해야 함
개수 차이를 서류에 표시함
- 조건을 만족하는 경우가 없으면 -1 리턴
"""

import sys
sys.stdin = open('sample_in.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_number = max(arr)
    # print(arr)

    # arr_little = []  # 소
    # arr_midium = []  # 중
    # arr_large = []  # 대

    counts = [0] * (max_number + 1)   # 0번 인덱스는 사용X
    for i in range(N):
        counts[arr[i]] += 1

    # 누적합 구하기
    for i in range(1, max_number+1):
        counts[i] = counts[i] + counts[i-1]

    # 당근 담기
    count = -1
    for i in range(max_number-2, 0, -1):  # little 범위
        for j in range(i+1, max_number):  # middle 범위
            # print(i, j)
            little = counts[i]
            middle = counts[j] - counts[i]
            large = counts[-1] - counts[j]
            if little > N//2 or middle > N//2 or large > N//2:
                # 이 경우에는 인정X
                continue
            # print(little, middle, large)
            max_box = max(little, middle, large)  # 세 상자 중 가장 큰 값
            min_box = min(little, middle, large)  # 세 상자 중 가장 작은 값
            differ = max_box - min_box
            # print(differ)
            if count == -1 or differ < count:
                count = differ
                # print('count 교환', count)

    # print(counts)
    print(f'#{test_case} {count}')

