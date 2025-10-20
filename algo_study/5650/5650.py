"""
5650_핀볼
"""

import sys
sys.stdin = open('sample_input.txt')

dr = [-1, 1, 0, 0]  # 이동 방향에 따라 인덱스 : 상하좌우
dc = [0, 0, -1, 1]

block = { # 해당 블록에 부딪혔을 때 방향이 어디로 변하는지
    1 : [1, 3, 0, 2],  # 현재 블록 -> 이동 방향 : 상 -> 하, 하 -> 우, 좌 -> 상, 우 -> 좌
    2 : [3, 0, 1, 2], # : 상 -> 우, 하 -> 상, 좌 -> 하, 우 -> 좌
    3 : [2, 0, 3, 1], # : 상 -> 좌, 하 -> 상, 좌 -> 우, 우, -> 하
    4 : [1, 2, 3, 0], # : 상 -> 하, 하 -> 좌, 좌 -> 우, 우 -> 상
    5 : [1, 0, 3, 2],  # : 상 -> 하, 하 -> 상, 좌 -> 우, 우 -> 좌
    # 나머지는 방향 안 바뀜(벽 빼고)
}

# DFS처럼
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # for i in range(N):
#     #     print(arr[i])

    # 어디에서 시작하든, 어느 방향으로 이동하든 모름
    # 이동 방향은 상하좌우

    hole = {
        6 : [],
        7 : [],
        8 : [],
        9 : [],
        10: []
    }

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 6:
                hole[6].append([r, c])
            elif arr[r][c] == 7:
                hole[7].append([r, c])
            elif arr[r][c] == 8:
                hole[8].append([r, c])
            elif arr[r][c] == 9:
                hole[9].append([r, c])
            elif arr[r][c] == 10:
                hole[10].append([r, c])

    # print(hole)

    max_count = 0

    cant_end=set({})  # 블랙홀 만나지 못하는 경우 저장

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                continue  # 블록, 웜홀, 블랙홀이 있는 위치에서는 출발할 수 없음
            for d in range(4):  # 상하좌우
                end_code = 1 # 블랙홀 만나서 끝나는지 여부
                ball = [r, c, d]
                count = 0
                route = set({})
                print('시작', ball, count, end_code)
                while arr[ball[0]][ball[1]] != -1:  # 블랙홀이 아닌 동안 반복
                    if count != 0 and [ball[0], ball[1]] == [r, c]:
                        print('처음 위치로 돌아옴')
                        break
                    if tuple(ball) in route:
                        print('블랙홀 만나지X')
                        cant_end = cant_end | route
                        end_code = 0
                        break
                    if tuple(ball) in cant_end:
                        break
                    route.add(tuple(ball))
                    if 1 <= arr[ball[0]][ball[1]] <= 5:  # 1~5 사이라면 방향 전환
                        ball[2] = block[arr[ball[0]][ball[1]]][ball[2]]
                        count += 1  # count 1 증가
                        print(arr[ball[0]][ball[1]], ball, '블록 부딪힘')
                    elif 6 <= arr[ball[0]][ball[1]] <= 10:  # 6~10 사이라면 위치 이동
                        print(arr[ball[0]][ball[1]], '웜홀')
                        if [ball[0], ball[1]] == hole[arr[ball[0]][ball[1]]][0]:
#                             # print(ball, hole[arr[ball[0]][ball[1]]])
                            ball[0], ball[1] = hole[arr[ball[0]][ball[1]]][1][0], hole[arr[ball[0]][ball[1]]][1][1]
#                             # print(ball[0], ball[1])

                        else:
                            ball[0], ball[1] = hole[arr[ball[0]][ball[1]]][0][0], hole[arr[ball[0]][ball[1]]][0][1]

                    # 2, 3, 4, 5, 6, 7, 8, 9, 10일때...
                    nr = ball[0] + dr[ball[2]]
                    nc = ball[1] + dc[ball[2]]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        print('벽 부딪힘')
                    #if not (0 <= nr < N and 0 <= nc < N) :  # 벽 밖이라면
                        # 방향 수정 -> 이건 bolck [5]와 동일함
                        ball[2] = block[5][ball[2]]
                        count += 1  # count 1 증가
                        # 다시 이동
                        nr = ball[0] + dr[ball[2]]
                        nc = ball[1] + dc[ball[2]]

                    # ball의 위치 갱신
                    ball[0] = nr
                    ball[1] = nc
                    print(ball, count)

                if end_code == 1:
                    print('블랙홀 만남', count)
                    if max_count < count:
                        print('갱신', count, max_count)
                        max_count = count

    # # 설마 이건 아니겠지만
    # max_count = max(0, max_count - 1)

    print(cant_end)

    print(f'#{test_case} {max_count}')