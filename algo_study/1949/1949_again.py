# 입력
import copy
import sys
sys.stdin = open('sample_input.txt')

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

    # 등산로 길이 카운트
    max_count = 1  # 제일 긴 count 찾기 / 현재 위치 포함해서 1로 시작함
    for d in range(4):  # 4방향
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:  # 벽체크
            # print(nr, nc, arr[nr][nc])
            if arr[nr][nc] < now_height:  # 더 낮으면
                # count += 1
                # 다음 실행, 현재 위치 값을 더해줌
                count = 1 + count_max_length(nr, nc, arr)

                # print(count)

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

    # 안 깎는 경우
    start = find_peek(arr)

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
                if len(start) == 1 and r == start[0][0] and c == start[0][1]:
                    continue
                arr_map = copy.deepcopy(arr)
                arr_map[r][c] -= i  # i 만큼 깎아냄
                #start = find_peek(arr_map)

                # print(start)

                for start_r, start_c in start:
                    # start_r, start_c = start[1]
                    result = count_max_length(start_r, start_c, arr_map)
                    if max_length < result:
                        max_length = result
    print(f'#{test_case} {max_length}')