"""
IM 기출문제 - 경비병

오랜시간 자습을 하던 당신은 그만 싸피 문이 닫힐 때까지 나오지 못하였다
탈출을 하기 위해서는 1층의 경비병의 눈에 띄지 않아야 한다
경비병은 자신의 위치로부터 상하좌우 N만큼 관찰을 할 수 있다 -> delta쓰는 문제구만
경비병의 시야에 기둥이 있다면 기둥 뒤는 인식하지 못한다
경비병의 눈을 피해 숨어있을 공간이 몇 개인지 출력

최초에 test_case 수가 주어짐
N 공간넓이
N줄만큼 경비병, 기둥, 공간 데이터가 주어짐

아마도 2가 경비병의 위치
1이 기둥인듯
"""

# 아이디어
"""
경비병의 위치에서부터 델타를 돌면서 1 만나거나 끝까지 가면서 0인 부분을 3으로 변경
그리고 나서 2차원 리스트 돌면서 0인 부분카운트
"""

import sys
sys.stdin = open('input.txt')


# 시작 위치 찾기
def find_guard(arr, N):
    """
    가디언의 위치를 찾는 함수
    :param arr: 공간 리스트
    :param N: 리스트의 행, 열 크기
    :return: 가디언의 위치 반환
    """
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


T = int(input())

# 델타
drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우 하 좌 상

for test_case in range(1, T + 1):
    # 입력 받기
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가디언의 위치 찾기
    gr, gc = find_guard(arr, N)  # 가디언의 위치 gr, gc

    # 델타 이용해서 순회하기
    for i in range(4):
        for j in range(1, N):
            nr = gr + drc[i][0] * j
            nc = gc + drc[i][1] * j

            # 벽 체크
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1:
                    break
                else:
                    arr[nr][nc] = 3

    # for i in range(N):
    #     print(arr[i])

    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count += 1
    print(f'#{test_case} {count}')