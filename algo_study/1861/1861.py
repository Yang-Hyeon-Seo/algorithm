"""
1861_정사각형 방_D4
N^2의 방이 NxN 형태로 늘어서 있음
위에서i번쨰 줄의 왼쪽에서 j번째 방에는 1이상 n^2의 수 Aij가 적혀 있음
이 숫자는 모든 방에 대해 서로 다름
내가 어떤 방에 있다면 상하좌우에 있는 다른 방으로 이동할 수 있음
- 이동하려는 방이 존재해야 함
- 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 함
처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있을까

델타 이용해서 만약 딱 1크다면 이동, 그리고 count 1 늘리기
N이 클 수 있기 때문에 재귀X
"""
import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]  # 오른쪽 아래 왼쪽 위
dc = [1, 0, -1, 0]


def count_move(r, c):
    """
    r, c에서 이동할 수 있는 숫자 세는 함수
    """
    count = 1  # 첫번째 방 포함
    # print(r, c, end=' ')
    while True:
        # print(arr[r][c], count)
        # Todo: 조건 설정하기
        # 내부 for문에서 return하기 때문에 그냥 무한루프
        # 델타 돌면서 이동하기
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
                # 벽 체크 and 현재 갑보다 정확히 1 크다면
                count += 1
                r = nr
                c = nc
                break
        else:
            # for문을 break로 탈출하지 않으면 현재 값보다 정확히 1 큰 곳이 없음
            # print()
            return count


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_move = 0
    move_number = N * N + 1  # 나올 수 없는 숫자임
    for r in range(N):
        for c in range(N):
            # 첫번째 방부터 마지막 방까지 이동
            now_move = count_move(r, c)
            # print('max_move', max_move, 'now_move', now_move)
            if (max_move < now_move) or (max_move == now_move and move_number > arr[r][c]):
                # print(max_move, now_move, move_number, arr[r][c])
                # max_move가 더 작으면 바꿔야 함
                # 또는
                # max_move가 같은데, move_number보다 더 작은게 나오면 바꿔야 함
                max_move = now_move  # 이동한 숫자
                move_number = arr[r][c]  # 방 숫자
                # print('갱신', 'max_move', max_move, 'move_number', move_number)
    print(f"#{test_case} {move_number} {max_move}")
