"""
백준 14499번

크기가 NxM인 지도
오른쪽이 동쪽, 위쪽이 북족

지도 위에 주사위가 있음

지도의 좌표는 r, c이며 북쪽에서 떨어진 칸의 개수, 서쪽으로부터 떨어진 칸의 개수임

지도 위에 윗면이 1이고 동쪽을 바라보는 방향이 3인 상태로 놓여져 있음
놓여져 있는 곳의 좌표는 x, y
가장 처음에 주사위에는 모든 면이 0이 적혀 있음

지도의 각 칸에는 정수가 하나씩 쓰여져 있음
주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면 주사위의 바닥면에 쓰여 있는 수가 칸에 복사됨
0이 아닌 수에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 됨

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때마다 상단에 쓰여 있는 값을 구하는 프로그램

"""

import sys
# sys.stdin = open('input.txt')

dx = [0, 0, 0, -1, 1]  # 0안씀, 동, 서, 북, 남
dy = [0, 1, -1, 0, 0]

# T = int(input())
# for test_case in range(1, T+1):
#
# N, M, x, y, K = map(int, input().split())
# arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))

N, M, x, y, K = map(int, sys.stdin.readline().strip().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
# dice = {  # 주사위 각 면의 값
#            1 : 0,
#            2 : 0,
#            3 : 0,
#            4 : 0,
#            5 : 0,
#            6 : 0,
# }

# 주사위 각 면의 값
dice = [0] * 7  # 0번째 인덱스 버림

# 현재 상태
# state = [2, 4, 1, 3, 5, 6]  # 북, 서, 위, 동, 남, 바닥 순서

# move_to = {  # 이동 방향에 따른 주사위 정렬
#     # 2, 4, 1, 3, 5, 6  (기본 정렬)
#     1 : [2, 6, 4, 1, 5, 3],
#     2 : [2, 1, 3, 6, 5, 4],
#     3 : [1, 4, 5, 3, 6, 2],
#     4 : [6, 4, 2, 3, 1, 5]
# }  # 1이라면 dice의 2번째 인덱스 값이 1번 인덱스로 가고, 6번 인덱스 값이 2번 인덱스로 가고... 그런 의미

move_to = {
    1 : [4, 2, 1, 6, 5, 3], # 기존 인덱스의 값들이 해당 위치로 이동함 dice[1] -> dice[3] 위치로 이동
    2 : [3, 2, 6, 1, 5, 4],
    3 : [5, 1, 3, 4, 6, 2],
    4 : [2, 6, 3, 4, 1, 5]
}
# pair = {  # key가 바다일 때 top인 면의 번호
#     1: 6,
#     2: 5,
#     3: 4,
#     4: 3,
#     5: 2,
#     6: 1,
# }

# print(x, y, '시작 위치')

result = []

bottom_idx = 6  # 바닥 인덱스
top_idx = 1  # 위 인덱스
# now_number = 0  # 현재 숫자
move = list(map(int, sys.stdin.readline().strip().split()))
for i in range(K):
    # print(f'{i} 번째 명령 : {move[i]}')
    nx = x + dx[move[i]]
    ny = y + dy[move[i]]
    # 벽 안에 안 들어오면 명령 무시해야 함
    if 0 <= nx < N and 0 <= ny < M:
        # 벽 안에 있음
        # print(nx, ny, '로 이동')
        # now_bottom = bottom[now_bottom][move[i]]  # 바닥 갱신
        # now_top = bottom[now_bottom][0]  # 현재 위 갱신

        dice = [0, dice[move_to[move[i]][0]], dice[move_to[move[i]][1]], dice[move_to[move[i]][2]], dice[move_to[move[i]][3]], dice[move_to[move[i]][4]], dice[move_to[move[i]][5]]]
        # 돌렸음
        x, y = nx, ny  # x, y 갱신


        if arr[x][y] == 0:
            # 주사위 바닥 면에 쓰여 있는 수가 주사위 칸에 복사됨
            # arr[x][y] = dice[now_bottom]
            arr[x][y] = dice[6]
        else:
            # 칸의 수가 주사위에 복사되며 칸의 수는 0이 됨
            dice[6] = arr[x][y]  # 주사위 면으로 복사
            arr[x][y] = 0

        result.append(dice[top_idx])

        # print(dice, 'bottom', dice[6], 'top', dice[top_idx])  # 6번이 항상 바닥, 3번이 항상 위
        # for i in range(N):
        #     print(arr[i])

        print(dice[top_idx])
# print(result)