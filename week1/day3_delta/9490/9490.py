'''
종이 꽃가루가 들어 있는 풍선이 M개씩 N개의 줄에 있음
어떤 풍선을 터뜨리면 현재 위치, 상, 하, 좌, 우에 꽃가루가 터짐
NxM개의 풍선에 들어 있는 종이 꽃가루 개수 A개 주어짐
한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합  중 최댓값

첫 줄에 테스트 케이스
첫 줄에 N과 M
리스트 안에 A 주어짐
'''

# 아이디어
'''
delta 이용하는데, delta마다 합을 구해서 전체 리스트 순회한 후에 delta 중에 가장 큰 것 출력
'''

# 문제 잘못 이해함
'''
종이 꽃가루가 들어 있는 풍선이 M개씩 N개의 줄에 있음
어떤 풍선을 터뜨리면 현재 위치, 상, 하, 좌, 우에 꽃가루가 터짐
NxM개의 풍선에 들어 있는 종이 꽃가루 개수 A개 주어짐
꽃가루 개수만큼 주변이 연쇄 폭발
한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합  중 최댓값
'''


# 입력 받기
import sys
sys.stdin = open('input1.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # delta 이동값
    rd = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위
    cd = [1, 0, -1, 0]

    # 가장 큰 값
    max_flower = 0

    # 리스트 [0][0]부터 순회하면서
    for r in range(N):
        for c in range(M):
            # 각 위치별 delta 합
            sum_flower = arr[r][c]  # 현재 위치

            if arr[r][c] == 0:
                # 만약 꽃가루가 안 들었다면
                sum_flower = 0
                continue

            # delta 이동
            for i in range(4):
                for a in range(1, arr[r][c]+1):
                    ri = r + rd[i] * a
                    ci = c + cd[i] * a

                    # 벽 확인
                    if 0 <= ri < N and 0 <= ci < M:
                        sum_flower += arr[ri][ci] # [ri][ci] 위치의 꽃가루의 양 만큼 더하기
            if sum_flower > max_flower: # 최대값 갱신
                max_flower = sum_flower
    print(f'#{test_case} {max_flower}')