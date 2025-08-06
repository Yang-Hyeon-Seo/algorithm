'''
5x5 2차 배열에 무작위로 25개의 숫자로 초기화한 후
25개 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절댓값 구하기
'''

# 값 입력
import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # 2차원 배열 만들기
    N = int(input()) # 정사각 배열의 행 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 배열 순회하면서 상하좌우 값이랑 기준값의 차이를 누적
    result = 0

    # 상하좌우 움직이기 위한 리스트
    dr = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽 위 순서
    dc = [1, 0, -1, 0]

    # 델타 순회
    for r in range(N):
        for c in range(N):
            #합 저장할 변수
            sum_number = 0
            # 좌표
            for i in range(4): #len(dr)
                ri = r + dr[i]
                ci = c + dc[i]

                # 범위 안에 해당하는지 확인
                if 0 <= ri < N and 0 <= ci < N:
                    # 범위 안에 해당하면 계산함
                    if arr[r][c] > arr[ri][ci]:
                        # 기준값이 더 크다면
                        sum_number += arr[r][c] - arr[ri][ci]
                    else:
                        sum_number += arr[ri][ci] - arr[r][c]
            result += sum_number

    print(f'#{test_case} {result}')