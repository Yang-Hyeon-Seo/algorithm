"""
4613_러시아 국기 같은 깃발
창고에서 오래된 깃발을 꺼내 옴
깃발은 N행M열로 나뉘어져 있고
각 칸은 흰색 파란색 빨간색 중 하나로 칠해져 있음
몇 개의 칸에 있는 색을 다시 칠해 이 깃발을 러시아 국기처럼 만들어야 함
위에서 몇줄은 모두 흰색으로 칠해져야 함
다음 몇줄은 모두 파란색으로 칠해져야 함
나머지줄은 모두 빨간색으로 칠해져야 함
칠해야 하는 칸의 개수의 최솟값 구하기
"""


# 완전 탐색

# blue가 1줄 ~ N-2줄동안
# blue가 1부터 n-2 사이에 위치하는 동안
# blue 위는 w
# blue 아래는 r로 바꾸는데
# 필요한 횟수


import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # arr = [input() for _ in range(N)]
    arr = [list(input()) for _ in range(N)]  # 출력 확인 위해 리스트로 변환

    # print(arr)

    count = 0
    # 첫 줄
    for a in arr[0]:  # a : alphabet
        if a != 'W':
            count += 1  # count만 하면 됨 일부러 바꿀 필요는 없음
    # print('1', count)
    # 두 번째 줄 ~ 마지막 직전 줄
    min_count = N*M  # 가장 큰 숫자 / 모든 칸이 바뀌어야 하는 N*M이 가장 큼

    for w in range(N-3, -1, -1):  # W가 가장 큰 때부터 점점 줄어듦
        for b in range(w+1, N-1):  # W의 바로 다음 줄부터 n-1까지 점점 확장
            middle_count = 0  # 중간부분 count라는 의미

            # w, b 번째 줄까지 다시 전체 리스트를 탐색하면서 count 계산
            for r in range(1, N-1):
                # 백트랙킹
                if middle_count > min_count:
                    # 이미 더 커졌음
                    break
                # print(arr[r])
                # 하기 전 0.05588s
                # 한 후 0.05750s
                # 의미가 없다~~

                if r <= w:
                    # for a in arr[r]:  # 문자열 돌면서 middle_count + 1
                    #     if a != 'W':
                    #         middle_count += 1
                    for a in range(M):  # 출력 확인하기 위해 수정
                        if arr[r][a] != 'W':
                            middle_count += 1
                            # arr[r][a] = 'W'
                elif r <= b:
                    # for a in arr[r]:
                    #     if a != 'B':
                    #         middle_count += 1
                    for a in range(M):  # 출력 확인하기 위해 수정
                        if arr[r][a] != 'B':
                            middle_count += 1
                            # arr[r][a] = 'B'
                else:
                    # for a in arr[r]:
                    #     if a != 'R':
                    #         middle_count += 1
                    for a in range(M):  # 출력 확인하기 위해 수정
                        if arr[r][a] != 'R':
                            middle_count += 1
                            # arr[r][a] = 'R'
                # print(arr[r], middle_count)

            # min_count와 비교해서 더 작으면 갱신
            if middle_count < min_count:
                min_count = middle_count

    count += min_count

    # 마지막 줄
    for a in arr[-1]:
        if a != 'R':
            count += 1

    print(f'#{test_case} {count}')