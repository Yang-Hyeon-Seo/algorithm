"""
1258_행렬찾기_im대비 문제

유엔 화학 무기 조사단이 대량 살상 화학 무기를 만들기 위해 화학 물질들이 저장된 창고를 조사하게 됨
창고에는 화작 물질 용기 n^2개가 nxn으로 배열되어 있었음
유엔 조사단은 각 용기를 조사하여 2차원 배열에 그 정보를 저장함
빈 용기에 해당하는 원소는 0으로 저장, 화학 물질이 들어있는 용기에 해당하는 용기는 화학 물질의 종류에 따라 1~9 사이의 정수를 저장

1. 화학물질이 담긴 용기들은 사각형을 이루고 있음, 사각형 내부에는 빈 용기 없음
2. 화학 물질이 담긴 용기들로 이루어진 사각형들은 각각 차원(가로용기수 x 세로용기수)이 다르다
3. 2개의 화학 물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다

2차원 배열에서 행렬(화학물질이 든 용기들로 이루어진 사각형)들을 찾아내고정보를 수집하고자 함

출력은 #{테스트케이스번호} {행렬수} {행} {열} .. (행렬수만큼) 이렇게 출력됨


확인한 행렬부분을 뛰어넘게 할 수 있을 것 같은데 일단 빨리 풀기 위해(속도는 느려지겠지만) 그냥 확인한 행렬을 0으로 바꿈
"""

import sys
sys.stdin = open('input (2).txt')


# result_list 정렬
def select_sort(result_list):
    N = len(result_list)
    for i in range(N):
        min_idx = i
        # min_number = result_list[i][-1]
        for j in range(i, N):  # 제일 작은 것 찾기
            if result_list[min_idx][-1] > result_list[j][-1]:
                min_idx = j
            elif result_list[min_idx][-1] == result_list[j][-1]:  # 둘의 크기가 같을때
                if result_list[min_idx][0] > result_list[j][0]:  # 지금의 행 크기가 더 작으면
                    min_idx = j
        # 제일 작은 것과 현재 위치 바꾸기
        result_list[i], result_list[min_idx] = result_list[min_idx], result_list[i]
    return result_list


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0  # 행렬의 수 계산
    result_list = []  # 정답 행렬을 (행, 열) 모양으로 append하기

    for r in range(N):
        for c in range(N):
            # 0이 아닌 것 만나면 어디까지 0이 아닌지 세기
            if arr[r][c] != 0:
                search_r = r

                while search_r < N and arr[search_r][c] != 0:  # r+1 벽치기 and 0이 아닌 동안(벽 조건 해당x 하면 뒤 조건 확인x)
                    search_c = c
                    while c < N and arr[search_r][search_c] != 0:
                        arr[search_r][search_c] = 0
                        search_c += 1
                    search_r += 1
                count += 1
                result_list.append((search_r-r, search_c-c, (search_r-r)*(search_c-c)))  # 행, 열, 크기 저장
            else:
                pass
    # print(count, result_list)
    result_list = select_sort(result_list)  # 행열의 크기가 작은 순서대로 출력
    # # 행렬의 크기가 같은 경우 행이 작은 순으로 출력
    # print(count, result_list)

    # 출력
    print(f'#{test_case} {count}', end=' ')
    for i in range(len(result_list)):
        print(' '.join(list(map(str, result_list[i][:2]))), end=' ')
    print()