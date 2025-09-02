"""
1949_등산로조성

NxN 크기의 부지
최대한 긴 등산로를 만들 계획
규칙
1. 등산로는 가장 높은 봉우리에서 시작해야 함
2. 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결되어야 함
3. 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 k 깊이만큼 지형을 깍는 공사를 할 수 있음

입력
NxN 크기의 지도
K
"""

# 입력
import copy
import sys
sys.stdin = open('sample_input.txt')
# sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]


# 재귀 사용하기
# def count_max_length(start, now_height, r, c, count):
def count_max_length(r, c, arr):
    """
    start : 시작 위치 들어가 있는 리스트
    now_height : 현재 높이
    r, c : 시작 위치
    count : 지금까지의 길이
    return : 여기서 최대 어디까지 갈 수 있는지
    """
    # 델타를 이용해서 4방향 탐색 -> 만약 더 낮은 곳이 있다면 그 방향으로 이동 후 count + 1

    # 현재 높이
    now_height = arr[r][c]
    # print(r, c, now_height)

    # 방문처리
    visited_arr[r][c] = 1

    # # 등산로 길이 카운트
    max_count = 1  # 제일 긴 count 찾기 / 현재 위치 포함해서 1로 시작함
    # 등산로 경로
    max_route = []
    for d in range(4):  # 4방향
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:  # 벽체크
            #print(nr, nc, arr[nr][nc])
            if arr[nr][nc] < now_height and visited_arr[nr][nc] == 0:  # 더 낮으면 and 방문X라면

                # count += 1
                # 다음 실행, 현재 위치 값을 더해줌
                count = 1 + count_max_length(nr, nc, arr)

                #print(count)

                if max_count < count:
                    max_count = count  # 가장 멀리갈 수 있는 값으로 갱신
        # 더 높거나 벽을 뚫으면 그냥 다음 델타 탐색
    return max_count

# 높이가 같은 곳도 연결 불가능하기 때문에 갔던 곳 다시 안 가도록 체크하는 것 안 해도 됨


# 가장 높은 곳 찾기
def find_peek(arr):
    max_height = 0  # 가장 큰 숫자 찾기
    for r in range(N):
        for c in range(N):
            if max_height < arr[r][c]:  # max_height 보다 높은 고도가 있다면
                max_height = arr[r][c]  # 갱신
    # 그 숫자에 해당하는 인덱스 저장하기(r, c) 형태의 튜플로
    start = []  # 가장 큰 숫자의 인덱스
    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_height:  # 가장 높은 곳이라면
                start.append((r, c))  # 튜플 형태로 저장
    return start


T = int(input())
for test_case in range(1, T + 1):

    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0

    # 방문 여부 체크
    visited_arr = [[0] * N for _ in range(N)]

    # 피크 먼저 찾고
    start = find_peek(arr)


    # 안 깎는 경우
    # print(start)

    for start_r, start_c in start:
        # start_r, start_c = start[1]
        result = count_max_length(start_r, start_c, arr)
        if max_length < result:
            max_length = result
    # 깎는 경우
    for i in range(1, K + 1):  # 0 ~ K 까지 하나씩 반복하면서 가장 긴 길이 찾기
        # [0][0]부터 [N][N]까지 하나씩 파면서 탐색
        for r in range(N):
            for c in range(N):
                # 만약 최고가 1개인데 거기를 깎는 경우 답이 될 수 없음
                if len(start) == 1 and (r, c) == start[0]:
                    continue
                arr_map = copy.deepcopy(arr)
                arr_map[r][c] -= i  # i 만큼 깎아냄
                # start = find_peek(arr_map)

                # print(start)

                for start_r, start_c in start:
                    # start_r, start_c = start[1]
                    result = count_max_length(start_r, start_c, arr_map)
                    if max_length < result:
                        max_length = result
    print(f'#{test_case} {max_length}')
