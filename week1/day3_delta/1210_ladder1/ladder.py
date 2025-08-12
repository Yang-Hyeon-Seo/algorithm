# 입력받기
import sys

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

총 10개의 테스트케이스가 주어짐
테스트케이스의 번호가 주어진 후 해당 테스트케이스의 100x100크기의 입력이 주어짐
'''

sys.stdin = open('input.txt')

# T = int(input())  # 반복 횟수
for _ in range(10):
    test_case = int(input())  # test case 번호
    N = 100  # 100x100이니까
    arr = [list(map(int, input().split())) for _ in range(N)]  # 100x100 사이즈이기 때문에

    # 이동
    rd = [0, 0, -1]  # 왼쪽, 오른쪽, 위
    cd = [-1, 1, 0]
    code = 2    # 이전 진행 상태 기록 / 위로 이동하는 것이 기본 (0으로 할지 고민하다가 delta랑 맞추기로 함)
    # code : 0 -> 왼쪽으로 이동함
    # code : 1 -> 오른쪽으로 이동함
    # code : 2 -> 위로 이동함

    # 2인 지점 찾기
    for c in range(N):  # 제일 마지막 행에서 찾으면 됨
        if arr[-1][c] == 2:
            start = c  # 탐색을 시작할 위치

    # 현재 위치
    r = N - 1  # 제일 마지막 행 인덱스가 99(100x100이니까)
    c = start

    # 반복하면서 이동
    while r > 0:  # r이 0보다 작아지면 종료
        for i in range(3):
            ri = r + rd[i]
            ci = c + cd[i]
            # 벽 확인 / 좌우 먼저 이동할거니까
            if 0 <= ci < N:  # r 항상 1 이상
                # 이동할 수 있는 칸 나오면 이동(위는 마지막에 확인하니까 괜춘)
                if arr[ri][ci] == 1:
                    # 이동 방향 고려
                    if code == 0:  # 이전에 왼쪽으로 이동했음(오른쪽으로 이동x)
                        if i == 1:
                            continue
                    elif code == 1:  # 이전에 오른쪽으로 이동했음
                        if i == 0:
                            continue

                    r, c = ri, ci
                    code = i
                    # if i == 2:
                    #     code = 2
                    break
    print(f'#{test_case} {c}')
