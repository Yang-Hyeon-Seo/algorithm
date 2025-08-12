"""
파리퇴치
NxN 배열 안의 숫자는 해당 영역에 존재하는 파리 개수 의미
MxM 크기의 파리채를 내리쳐 최대한 많은 파리를 죽이고자 함
죽은 파리의 개수 구하기
테스트케이스
N, M
NxN배열
순서대로 입력
"""

import sys
sys.stdin = open("input.txt")

for i in range(0):
    print(i)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_killed = 0

    for r in range(N):
        for c in range(N):
            killed_fly = 0
            # MxM 크기 순회
            for m in range(M):
                for n in range(M):
                    nr = r + m
                    nc = c + n

                    if 0 <= nr < N and 0 <= nc < N:
                        killed_fly += arr[nr][nc]

            if killed_fly > max_killed:
                max_killed = killed_fly

    # for r in range(N-M):
    #     for c in range(N-M):
    #         killed_fly = 0
    #         # MxM 크기 순회
    #         for m in range(M):
    #             for n in range(M):
    #                 nr = r + m
    #                 nc = c + n
    #                 killed_fly += arr[nr][nc]
    #
    #         if killed_fly > max_killed:
    #             max_killed = killed_fly



    print(f'#{test_case} {max_killed}')





