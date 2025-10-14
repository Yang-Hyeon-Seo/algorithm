"""
2117_홈 방범 서비스
"""

import sys
sys.stdin = open('sample_input.txt')


dr = [0, 1, 0, -1]  # 우, 하, 좌, 상
dc = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타
    count = 0
    for i in range(N):
        count += arr[i].count(1)

    max_house = 0

    K = 1
    while (2 * K * (K - 1)) < count * M:
        for r in range(N):
            for c in range(N):
                house_num = arr[r][c]
                for k in range(1, K):
                    for d in range(4):
                        nr = r + k * dr[d]
                        nc = c + k * dc[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            house_num += arr[nr][nc]
                if house_num * M > 2 * K * (K - 1) and max_house < house_num:
                    max_house = house_num
        if max_house == count:
            break
        K += 1

    print(f"{test_case} {max_house}")