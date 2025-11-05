"""
상어 중학교
NxN 격자에서 진행
초기 격자의 모든 칸에는 블록이 하나씩 들어 있고, 블록은 검은색, 무지개, 일반 블록이 있음
일반 블록은 M가지 색상이 있고, 색은 M 이하의 자연수로 표현함
검은색 블록은 -1, 무지개 블록은 0임
(i, j)는 격자의 i번 행, j번 열을 의미
|r1-r1| + |c1-c2| = 1을 만족하는 두 칸과 인접한 칸이라고 함(행만 다르거나 열만 1칸 차이남)

블록 그룹은 연결된 블록의 집합.
그룹에는 일반 블록이 적어도 하나 있어야 함.
일반 블록의 색은 모두 같아야 함

검은색 블록은 포함되면 안되고 무지개 블록은 얼마나 들어 있든 상관 없음
그룹에 속한 블록의 개수는 2보다 크거나 같아야 함
임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로이동할 수 있어야 함

블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록
그런 블록이 여러개면 열의 번호가 가장 작은 블록임

이 게임의 오토 플레이 기능을 만들거임
다음과 같은 블록 그룹이 존재하는 동안 계속해서 반복되어야 함

1. 크기가 가장 큰 블록 그룹을 찾음
그러한 블록이 여러개라면 포함된 무지개 수가 가장 많은 블록 그룹
그러한 블록도 여러개면 기준 블록의 행이 가장 큰 것, 그것도 여러개면 열이 가장 큰 것을 찾음
2. 1에서 찾은 블록의 모든 블록을 제거함
블록 그룹에 포함된 블록의 수를 B라고 했을 때 B제곱 점을 획득함
3. 격자에 중력이 작용
4. 격자가 90도 반시계 방향으로회전함
5. 격자에 중력이 작용함

다시 1번부터 돌아감

격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동함
이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속됨
오토플레이가 끝났을 때 획득한 점수의 합을 구하기
"""

import sys
from collections import deque
# sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

def find_big(arr, N):
    """
    크기가 가장 큰 블록 그룹을 찾는 함수
    """
    groups = []  # (블록 그룹 크기, 가장 위/왼쪽인 기준 블록의 r,c)를 리스트로 저장
    visited = [[0] * N for _ in range(N)]  # 이미 그룹에 해당한다면 1, 그룹에 해당하지 않는다면 0

    # for i in range(N):
#     #     print(visited[i])

    zero_list = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] == -2 or arr[r][c] == -1 or arr[r][c] == 0 or visited[r][c] == 1:
                # 빈 칸 검은 블록 or 무지개 블록 or 이미 그룹에 해당하는 블록이라면 스킵
                continue
            number = arr[r][c]

            visited[r][c] = 1  # 방문처리 먼저 하고, 큐에 삽입
            q = deque()  # (r, c) 형태의 튜플을 집어 넣음
            q.append((r, c))
            # print(q)
            count = 1
            zero_list.clear()



            while q:  # q가 비어있지 않는 동안
                now_r, now_c = q.popleft()
                # 현재 기준으로 델타를 돌음
                for i in range(4):
                    new_r = now_r + dr[i]
                    new_c = now_c + dc[i]
                    # print(new_r, new_c)
                    if 0 <= new_r < N and 0 <= new_c < N:
                        if (arr[new_r][new_c] == number or arr[new_r][new_c] == 0) and visited[new_r][new_c] == 0:
                            if arr[new_r][new_c] == 0:
                                zero_list.append((new_r, new_c))
                            visited[new_r][new_c] = 1  # 방문처리
                            q.append((new_r, new_c))
                            count += 1

                            # for j in range(N):  # 변화 출력
                #                 print(visited[j])
                # print(q, count)
            zero_blocks = len(zero_list)
            for i in range(zero_blocks):
                zr, zc = zero_list[i]
                visited[zr][zc] = 0  # 무지개 블록 방문처리 취소

            # print('무지개블록 돌려놓음')
            # for i in range(N):
                # print(visited[i])

            if count > 1:
                groups.append((count, zero_blocks, r, c))

    # 블록 그룹이 없다면
    if len(groups) == 0:
        return 0

#     # print(groups)
    groups.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    # print(groups)

    # 이제 제일 큰 녀석을 지움
    # 빈 칸은 -2로 표시
    w, z, r, c = groups[0]
    number = arr[r][c]  # 현재 값 받고

    arr[r][c] = -2  # 칸을 비우고, 큐에 삽입
    q = deque()  # (r, c) 형태의 튜플을 집어 넣음
    q.append((r, c))
#     # print(q)

    while q:  # q가 비어있지 않는 동안
        now_r, now_c = q.popleft()
        # 현재 기준으로 델타를 돌음
        for i in range(4):
            new_r = now_r + dr[i]
            new_c = now_c + dc[i]
#             # print(new_r, new_c)
            if 0 <= new_r < N and 0 <= new_c < N:

                if arr[new_r][new_c] == number or arr[new_r][new_c] == 0:  #) and visited[new_r][new_c] == 0:
                    arr[new_r][new_c] = -2  # 지우고
                    q.append((new_r, new_c))  # 지운 위치 큐에 추가

    # for i in range(N):
        # print(arr[i])


    return w ** 2  # 제곱값 반환


def gravity(arr, N):
    """
    열 기준 순회
    행은 아래에서부터 돌면서
    -2를 만나면 위의 값을 확인해서
    -1을 만나면 그 위에서부터 다시 -2인지 여부 확인
    다른 값을 만나면 처음 -2인 곳으로 해당 값을 바꾸고 그 위치에 -2를 저장
    """
    for c in range(N):
        # print(c, '열')
        r = N - 1
        empty_r = -1
        while r >= 0:  # r이 0 이상인 동안 반복
            # print(r, 'r 확인', empty_r, 'empty_r 확인')

            if empty_r < 0 : # 빈 곳 없을 때
                if arr[r][c] == -2 : # -2를 처음 만나면
                    # print('처음 빈곳 만남')
                    empty_r = r  # 처음 비어있는 r의 위치 저장
                else:  # 다른 곳 만나면
                    pass  # 딱히 뭐 하지 않음

            else:
                if arr[r][c] == -2:
                    # 처음 아니지만 빈 곳 만남
                    # print('처음 아니지만 빈 곳 만남')
                    pass
                elif arr[r][c] == -1: # 검은 블록
                    # print('검정')
                    empty_r = -1  # 다시 empty_r을 초기화
                else: # 일반 블록
                    # print('일반')
                    arr[empty_r][c] = arr[r][c]  # 값을 바꿔주고
                    arr[r][c] = -2  # 현재 위치 값 비워주고
                    empty_r -= 1  # 제일 아래 비어 있는 칸 하나 올려주고

            r -= 1

            # for i in range(N):
                # print(arr[i])


def gravity_rotation_gravity(arr, N):
    """
    반시계 방향으로 90도 회전하고 중력을 적용하는 함수
    """

    gravity(arr, N)

    rotated = list(map(list, zip(*arr[:])))[::-1]

    gravity(rotated, N)

    #arr = rotated.copy()
    return rotated

# T = int(input())
# for test_case in range(1, T+1):
N, M = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# for i in range(N):
# #     print(arr[i])

r = 1
result = 0
while r != 0:  # r이 0이 아닌 동안
    r = find_big(arr, N)
    result += r  # 더하기
    arr = gravity_rotation_gravity(arr, N)  # 돌리기
    # print(r, result)

print(result)