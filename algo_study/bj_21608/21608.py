"""
백준_21608번

"""
import sys
# sys.stdin = open("input.txt")

dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]


def find_sit(arr, friends, i, N):
    """
    자리 찾아서 배정하는 함수
    """
    # print(f'-------------{i}에 대해 계산---------------')
    # friends_num = [[0] * N for _ in range(N)]
    max_friend_count = 0
    max_empty_count = 0
    max_sit = (0, 0, 0, 0) # (r, c, 친구수, 빈자리 수)
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if arr[r][c] != 0:  # 해당 위치가 이미 차지되었다면
                continue
            friend_count = 0
            empty_count = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 < nr <= N and 0 < nc <= N:
                    if arr[nr][nc] == 0:  # 비어 있는 자리 구함
                        empty_count += 1
                        # print(nr, nc, 'empty_count', empty_count)

                    elif arr[nr][nc] in friends[i]:  # 선호 친구 수 구함
                        friend_count += 1
                        # print(nr, nc, 'friend_count', friend_count)

            if max_friend_count < friend_count:  # 1 만족 -> 갱신
                max_sit = (r, c, friend_count, empty_count)
                max_friend_count = friend_count
                max_empty_count = empty_count
                # print('갱신', r, c, friend_count, empty_count)

            elif max_friend_count == friend_count:  # 1만족하는게 여러개
                if max_empty_count < empty_count: # 빈자리가 가장 큰 것 선택
                    max_sit = (r, c, friend_count, empty_count)
                    max_empty_count = empty_count
                    # print('빈자리 큰 곳으로 갱신', r, c, friend_count, empty_count)

    # print('최종', max_sit[0], max_sit[1], i)  # , max_friend_count, max_empty_count)

    #비어있지도 않고 친구도 근처에 없는 마지막 1자리인 경우엔?
    if max_sit[0] == 0 or max_sit[1] == 0:  # 자리가 지정되지 않음
        for r in range(1, N+1):
            for c in range(1, N+1):
                if arr[r][c] == 0:
                    # print('제일 먼저 오는 빈 자리')
                    arr[r][c] = i
                    return None

    else:
        arr[max_sit[0]][max_sit[1]] = i


    # for i in range(1, N+1):
    #     print(arr[i][1:])

    return None



# T = int(input())
# for test_case in range(1, T+1):
N = int(sys.stdin.readline().strip()) # int(input()) #

arr = [[0] * (N + 1) for _ in range(N + 1)]  # 0번 인덱스 버림

friends = {}
sequence = []

for i in range(1, N * N + 1):
    num, f1, f2, f3, f4 = map(int, sys.stdin.readline().strip().split())  # map(int, input().split())#
    friends.setdefault(num, (f1, f2, f3, f4))
    sequence.append(num)

# print(N)
# for i in range(N + 1):
#     print(arr[i])
# print(friends)
# print(sequence)

for i in range(N * N):
    find_sit(arr, friends, sequence[i], N)

# for i in range(1, N+1):
#     print(arr[i][1:])

result = 0
# 이제 인접한 자리의 좋아하는 학생 수 구하기
for r in range(1, N + 1):
    for c in range(1, N + 1):
        count = 0
        # print(arr[r][c])
        for d in range(4):
            # 델타 돌면서 인접한 곳에 좋아하는 친구 몇 명인지 세기
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 < nr <= N and 0 < nc <= N and arr[r][c] != 0 and arr[nr][nc] in friends[arr[r][c]]:
                count += 1
                # print(arr[nr][nc], end=' ')
        # print()
        if count > 0:
            result += 10 ** (count - 1)
            # print(result)

print(result)