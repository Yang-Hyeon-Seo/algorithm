"""
2382_미생물 격리
"""


import sys
sys.stdin = open("sample_input.txt")


# 델타
dr = [0, -1, 1, 0, 0]  # 0번 인덱스 버림, 상, 하, 좌, 우
dc = [0, 0, 0, -1, 1]

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    arr = []
    for i in range(N):
        if i == 0 or i == N-1:
            arr.append([1] * N)
        else:
            arr.append([1] + [0] * (N-2) + [1])
    # for i in range(N):
#     #     print(arr[i])

    groups = []
    for i in range(K):
        groups.append(list(map(int, input().split())))
    # for i in range(N):
#     #     print(groups[i])

    # visited = [[(0, 0)] * N for _ in range(N)]  # 방문 상태 저장
    # for i in range(K): #  groups:
    #     visited[groups[i][0]][groups[i][0]] = (1, i)   # (방문, 인덱스)

    for time in range(M):
        # 시간 지날 때마다 확인
        # print('시간', time)
        # for i in range(K):
#         #     # print(groups)
#         #     print(groups[i])
        #     if groups[i][2] == 0:
        #         continue
        #
        #
        #     nr = groups[i][0] + dr[groups[i][3]]
        #     nc = groups[i][1] + dc[groups[i][3]]

            # 어차피 경계에서 방향을 바꾸기 때문에 벽체크할 필요 없음

            # 아래 주석 -> 이렇게 하면 동시에 이동할거라서 그 칸에 없을건데 인덱스가 뒤에 있어서
            # 일시적으로 겹쳐지는 경우에도 아래 코드를 작동시켜서 안될듯
            # # 이동할 곳에 이미 군집이 자리하고 있다면
            # if visited[nr][nc] == 1:
            #     # 두 군집을 합쳐야 함(큰쪽으로)
            #     if groups[i][2] > groups[visited[groups[i][0]][groups[i][1]][0]][2]:
            #         groups
            #
            # # 기존 visited 를 비워주고, 새로운 visited로 이동
            # visited[group[0]][group[1]] = 0
        for group in groups:
            # # print(groups)
            # print(group)
            if group[2] == 0:
                continue


            nr = group[0] + dr[group[3]]
            nc = group[1] + dc[group[3]]

            group[0] = nr
            group[1] = nc

            # print('이동')

            if arr[nr][nc] == 1:  # 경계에 도달
                group[2] = group[2] // 2  # 절반으로 줄어듦
                # 방향 바꾸기
                if group[3] == 1:
                    group[3] = 2
                elif group[3] == 2:
                    group[3] = 1
                elif group[3] == 3:
                    group[3] = 4
                elif group[3] == 4:
                    group[3] = 3
                # print('방향 전환', group[2], '만큼 남음')

            # print(group)

        # print('겹침 확인')
        # 이동 다한 후에 혹시 좌표 겹치는게 있는지 확인
        arr_now = [[[] for i in range(N)] for _ in range(N)]  # 빈 이중 리스트 생성
        for i in range(K):
#             # print(groups[i])
#             # print(groups[i][0])
#             # print(groups[i][1])
#             # print(arr_now[groups[i][0]][groups[i][1]])
            arr_now[groups[i][0]][groups[i][1]].append((groups[i][2], i))  # 남은 생물 수, groups 인덱스 번호 추가함

        # for i in range(N):
            # print(arr_now[i])

            # 2개 이상이면 겹침
        for i in range(N):
            for j in range(N):
                if len(arr_now[i][j]) > 1:
                    # 겹쳤다면
                    tmp_group = arr_now[i][j].copy()  # 복사
                    tmp_group.sort(reverse=True)  # 내림차순 정렬
                    # print(tmp_group)
                    for index in range(1, len(tmp_group)):
                        # 0번에 다 몰아넣고, index는 비우기
                        groups[tmp_group[0][1]][2] += tmp_group[index][0]
                        groups[tmp_group[index][1]][2] = 0
                    # print(groups[tmp_group[0][1]][2])
                    # print(groups[tmp_group[1][1]][2])

                    # for group in range(len(arr_now)):
                    #     tmp_group.append([groups[arr_now[i][j][group]][2], arr_now[i][j][group]])
                    # tmp_group.sort(reverse=True)  # 내림차순으로 정렬
                    # for group in range(1, len(arr_now)):
                    #     groups[tmp_group[0][1]][2] += groups[tmp_group[group][2]]  # 합치고
                    #     groups[tmp_group[group][1]][2] = 0  # 작은쪽거 없애기

        # 아래의 경우 3개 이상 겹칠 때 오류가 발생할 수 있음
        # for i in range(K):
        #     for j in range(i+1, K):
        #         # i 뒤에서부터 끝까지 돌면서 세로, 가로 같으면 군집이 겹치게 됨
        #         if groups[i][0] == groups[j][0] and groups[i][1] == groups[j][1]:
        #             # 군집 겹침
#         #             print('군집겹침')
        #             if groups[i][2] > groups[j][2]:  # i번째 군집의 개체수가 더 큰 경우
#         #                 print(i, '가', j, '보다 큼')
        #                 groups[i][2] += groups[j][2]  # 더하고
        #                 groups[j][2] = 0  # 0으로 만들기
        #
        #             else:
#         #                 print(j, '가', i, '보다 큼')
        #                 groups[j][2] += groups[i][2]
        #                 groups[i][2] = 0
#         #             print(groups[i])
#         #             print(groups[j])


    count = 0
    for group in groups:
        count += group[2]

    print(f'#{test_case} {count}')