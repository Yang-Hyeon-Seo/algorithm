'''
파리퇴치3
NxN배열 안의 숫자는 해당 영억에 존재하는 파리의 개체수 의미
파리 킬러 스프레이를 통해 최대한 많은 파리를 잡으려고 함
스프레이는 + 또는 x방향으로 분사됨
중심적으로부터 M칸 떨어진 곳의 파리를 잡을 수 있음

delta 이용하기
'''

def delta_max_killed_fly (arr, dr, dc, N, M):
    '''
    dr, dc 따라가면서 몇마리 죽였는지 최대값 리턴하는 함수
    '''
    max_killed = 0
    for r in range(N):
        for c in range(N):
            # 죽인 파리 수 카운트
            killed_fly = arr[r][c]  # 현재 위치 파리 수
            for i in range(len(dr)):
                for m in range(1, M):  # m이 현재 위치 포함하는지/아닌지 확인 필요(포함X)                #delta 탐색
                    nr = r + m * dr[i]
                    nc = c + m * dc[i]
                    # 벽 확인
                    if 0 <= nr < N and 0 <= nc < N:
                        # 충족하는 경우에
                        killed_fly += arr[nr][nc]
            # print('killed', killed_fly)
            if  killed_fly> max_killed:
                max_killed = killed_fly
    return max_killed

# 입력받기
import sys
sys.stdin = open('in1.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #< +로 분사하는 경우>
    # delta
    # +
    dr = [-1, 1, 0, 0] #상 하 좌 우
    dc = [0, 0, -1, 1]

    # 가장 많이 죽인 수
    max_killed1 = delta_max_killed_fly(arr, dr, dc, N, M)
    # print('+', max_killed1)



    #< x로 분사하는 경우>
    # delta
    # +
    dr = [-1, 1, 1, -1] #상우 하우 하좌 상좌
    dc = [1, 1, -1, -1]
    max_killed2 = delta_max_killed_fly(arr, dr, dc, N, M)
    # print('x', max_killed2)


    # 둘 중에 더 큰 수
    if max_killed1 >= max_killed2:
        print(f'#{test_case} {max_killed1}')
    else:
        print(f'#{test_case} {max_killed2}')