'''
사다리 타고 내려가면서 (올라가지 x)
아래 말고 다른 방향으로 이동할 수 있는 경우 거기로 이동
도착지점인 2로 도착하는 출발지 찾기
'''

# 아이디어
'''
2인 지점에서 시작해서
위로 올라가되
위 말고 다른 방향이 나오면 그 방향으로 이동(아래는 아예 고려X)
rd = [0, 1, 0] # 왼쪽, 위, 오른쪽
cd = [-1, 0, 1]
이렇게
그리고 위쪽 벽에 닿는 순간의 X 위치를 반환
delta로 이동할 때 ri가 0보다 작아지는 순간이 오면 종료
언제 끝날지 모르니까 while True 사용하기
'''

# 입력받기
import sys
sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1, T + 1):
    N = 100 # 100x100이니까
    arr = [list(map(int, input().split())) for _ in range(N)] # 100x100 사이즈이기 때문에

    # 이동
    rd = [0, -1, 0]  # 왼쪽, 위, 오른쪽
    cd = [-1, 0, 1]

    # 2인 지점 찾기
    for c in range(N): # 제일 마지막 행에서 찾으면 됨
        if arr[-1][c] == 2:
            start = c # 탐색을 시작할 위치

    # 현재 위치
    r = 99 # 제일 마지막 행 인덱스가 99(100x100이니까)
    c = start

    # 반복하면서 이동
    while True:
        for i in range(3):
            ri = r + rd[i]
            ci = c + cd[i]

            # 벽 확인
            if ri - 1 < 0:
                x = c
                break
            elif 0 <= ci < N:
                # 이동할 수 있는 칸이면 이동
                if #좌우 먼저 확인
                # 아니면 위로 이동