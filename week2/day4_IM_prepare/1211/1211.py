"""
1211_ladder2
사다리타기게임

100x100 크기의 2차원 배열로 주어진 사다리에 대해서 모든 출발점을 검사하여
바닥까지 가장 짧은 이동 거리를 갖는 시작점을 반환하는 프로그램 작성
길이가 같다면 가장 큰 x좌표 반환

여기에서는 간 길을 0으로 바꾸면 다음을 검사하지 못함..
이전에 활용했던 방법인 code를 사용해보자!

그리고 0으로 바꾸면서 진행하는 코드를 생각해보자 (근데 그러면 복사해서 진행해야 할 것 같은데?)
"""

# 이중 리스트의 0번부터 시작
# 위에서 아래로 이동
# 이동할 때마다 count + 1
# max_count보다 크면 갱신

import math, sys
sys.stdin = open('input.txt')

# 델타
drc = [[0, -1], [0, 1], [1, 0]]  # 좌, 우, 하 탐색 / 한 번에 만들어 보고 싶어서 이렇게 만듦

T = 10
for tc in range(1, T + 1):
    test_case = int(input().strip())  # 입력에 좌우 공백 제거해서 받고, 숫자로 변경
    N = 100  # 2차원 배열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_count = math.inf  # 가장 짧은 거리 저장, 무한대로 초기화
    min_c = 0  # 첫번째 출발지점으로 초기화
    for c in range(N):
        # 첫번째 행의 c번째 위치에서 시작
        if arr[0][c] != 1:  # 1이 아니면 시작 위치 아님
            continue
        # 시작 위치라면 이제 아래로 이동하면서 길 찾아야 함
        r = 1  # 일단 1칸 내려와서 시작함(첫번째 행에서 1인 지점은 출발지점, 옆으로 이동하지 X
        start_c = c
        count = 1  # 한 칸 이동한 행부터 시작하니까 초기값은 1

        # print('시작', r, c, count)

        while r < N-1:  # 마지막 행 전까지 돌아야 함
            for i in range(3):  # 델타가 좌, 우, 하 3가지이기 때문에
                # nr = r + drc[i][0]
                nc = c + drc[i][1]
                # 벽 체크
                if 0 <= nc < N:  # 0 <= nr < N and 0 <= nc < N:
                    # 벽 안에 있다면 이동
                    if arr[r][nc] != 1:
                        # 1이 아니면 이동x, 다음 델타 확인
                        continue
                    # 여기서 0으로 바꾸면 다시 돌아오지 않지만, arr이 바뀌어서 다음을 시작점을 확인할 수 없음
                    # 우성님 하셨던 것 처럼 while 통해서 그 방향으로 쭉 가고, 아래로 1칸 이동하게 하기
                    # 조건문 안 쓰려고 했는데, 그러면 아래로 2칸씩 내려간다는 문제가 있음
                    # 좌 우 이동 끝나고 바로 내려가지 않으면 무한루프에 빠짐
                    # 그래서 if 문으로 좌우 반복 끝나고 한 칸 내려가면 아래로 이동하는 델타 검토하지 않고 바로 break
                    if i < 2:
                        while i < 2 and 0 <= nc < N and arr[r][nc] == 1:  # i가 좌 또는 우 & 새로운 좌표가 1이면 쭉 이동
                            # 벽 체크를 중간에 해서 만약 false 라면 그 뒤 조건을 검사하지 않음
                            c = nc  # r은 이동하지 않으니까 그대로 두기
                            count += 1  # 이동했으니까 +1
                            nc = c + drc[i][1]

                            # print('옆으로 이동', r, c, count, i, arr[r][c])

                            # # 벽체크
                            # if 0 > nc or nc > N:  # 벽 밖으로 나가면 break
                            #     break

                        r += 1  # 좌/우 이동 끝나면 r에 1을 더해줌
                        # 위에서 이동할 값이 1이 아니면 continue 하기 때문에 행 이동을 여러번하지 않음(아마도)
                        count += 1  # 이동했으니까 +1

                        # print('아래로 이동', r, c, count, i, arr[r][c])
                        break

                    else:
                        r += 1  # 아래로 이동
                        count += 1  # 이동했으니까 +1

                        # print('아래로 이동', r, c, count, i, arr[r][c])

        # print('값 비교', min_count, count, start_c)
        if min_count >= count:
            min_count = count
            min_c = start_c

    print(f'#{test_case} {min_c}')