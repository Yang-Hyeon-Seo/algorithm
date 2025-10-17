"""
5644_무선충전
"""

import sys
sys.stdin = open('sample_input.txt')


# 이동 방향
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]  # 이동X, 상, 우, 하, 좌

T = int(input())
for test_case in range(1, T+1):
    N = 10  # 영역 크기
    M, A = map(int, input().split())  # M : 이동 정보 길이, A : BC의 개수

    # user1 = list(map(int, input().split()))  # A의 이동 경로
    # user2 = list(map(int, input().split()))  # B의 이동 경로

    user_location = {1:[1, 1, []], 2:[10, 10, []]}  # 사용자 번호에 따른 위치 저장
    # 딕셔너리 이용해보고 싶어서 사용
    # [x, y, (현재 이용할 수 있는 충전기 성능, 충전기 번호)가 채워질 것

    users = []
    users.append(list(map(int, input().split())))
    users.append(list(map(int, input().split())))  # 2명이니까 2번 append

    BC = []  # 배터리 정보 담긴 리스트
    for bc in range(A):
        BC.append(list(map(int, input().split())))

    arr = [[0] * N for _ in range(N)]
    # 해당하는 칸 구해서 미리 계산하려고 했는데 그냥 초별로 움직이기로 함
    # for bc in BC:
    #     r = bc[1]
    #     c = bc[0]
    #     for i in range(bc[2]):

    result = 0  # 충전 성능 합

    for time in range(M+1):  # 시간이 0일때부터 M일때까지 반복
        check_power = 0  # power 확인해야 한다는 것 확인하는 변수
        count = 0  # 현재 위치의 충전 성능 더하기

        # print('현재시간', time, '-------------------------')
        # 매 시간별로 거리 확인해서 계산하기
        for user in range(1, 3):  # 사용자별로 반복
            # 사용자 위치 받기
            x, y, can_use_bc = user_location[user]  # c, r 순서임에 주의
            # can_use_bc의 경우에는 해당 리스트 위치를 받기 때문에 그냥 쓰면 됨
            can_use_bc.clear()  # 기존에 들어있던 것 지우기 먼저 하기

            for i in range(A):
                distance = abs(x-BC[i][0]) + abs(y-BC[i][1])
                if distance <= BC[i][2]:
                    can_use_bc.append((BC[i][3], i))  # (충전 성능, 충전기 번호)
            if len(can_use_bc) > 0:
                check_power = 1

            # print(user, '번', x, y, can_use_bc)
            # 위치 다 받았으니까 이동하기
            if time < M:
                user_location[user][0] = x + dx[users[user-1][time]]
                user_location[user][1] = y + dy[users[user-1][time]]
                # print(user, '다음위치', user_location[user])
        # 위치와 거리 다 받았음

        if check_power == 1:
            # print('충전함')
            # 누구라도 일단 충전할 수 있음
            user1_bc = user_location[1][2].copy()  # 연결할 수 있는 배터리 리스트
            user1_bc.sort(reverse=True)
            # print(user1_bc)

            user2_bc = user_location[2][2].copy()
            user2_bc.sort(reverse=True)

            # print(user2_bc)
            # 내림차순으로 정렬


            # 둘 다 어딘가에 소속되어 있는 경우
            if len(user1_bc) > 0 and len(user2_bc) > 0:
                max_user1 = user1_bc[0]
                max_user2 = user2_bc[0]
                # 내림차순으로 정렬해서 가장 앞이 충전 성능이 가장 큼

                # max가 같은 경우(같은 충전기인 경우)
                if max_user1 == max_user2:
                    # 근데 둘 다 들어갈 수 있는 충전기가 하나인 경우
                    if len(user1_bc) == 1 and len(user2_bc) == 1:
                        count = max_user1[0]
                    elif len(user1_bc) > 1 and len(user2_bc) > 1:
                        # 둘 다 들어갈 수 있는 충전기가 2개임
                        count = max_user1[0]
                        count += max(user1_bc[1][0], user2_bc[1][0])
                    elif len(user1_bc) == 1:
                        # user2_bc가 2개 이상이면
                        count = max_user1[0]
                        count += user2_bc[1][0]
                    elif len(user2_bc) == 1:
                        # user1_bc가 2개 이상이면
                        count = max_user2[0]
                        count += user1_bc[1][0]
                else:
                    # max가 다른 경우
                    count = max_user1[0]
                    count += max_user2[0]

            # 둘 중 하나만 들어가 있으면 그냥 큰 것 뽑아내면 됨
            elif len(user1_bc) > 0:
                # user1_bc만 1개 이상인 경우
                count = user1_bc[0][0]

            elif len(user2_bc) > 0:
                # user2_bc만 1개 이상인 경우
                count = user2_bc[0][0]

            # 둘 다 어디에도 소속이 안되어 있으면 -> 할거 없음
            # print(count)

            result += count
            # print('result', result)
        # 1. 일단 어디든 연결되어 있으면 충전함
        # 2. 사람이 겹치면(같은 충전기를 이용하게 되면)
        # 2-1. 가능하면 서로 다른 충전기 이용
        # 2-2. 같은 충전기라면 그냥 한 사람만 카운트하기

    # 모든 사용자의 충전양 합치기
    print(f'#{test_case} {result}')