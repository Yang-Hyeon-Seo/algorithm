"""
2115_벌꿀채취
NxN개의 벌통이 정사각형 모양으로 배치됨
각 칸의 숫자는 벌통에 있는 굴의 양 의미

각 통에 있는 꿀의 양이 주어졌을 때
다음의 과정으로 벌꿀을 채취하여 최대한 많은 수익을 얻으려고 함
1. 두명의 일꾼이 있음
꿀을 채취할 수 있는 벌통의 수 M
각각의 일꾼은 가로로 연속이 되도록 M개의 벌통을 선택하고 꿀을 채취할 수 있음
단, 벌통이 서로 겹치면 안됨

2. 두명의 일꾼은 선택할 벌통에서 꿀을 채취하여 용기에 담음
하나의 벌통에서 꿀을 채취할 때 모든 꿀을 한번에 다 채취해야 함
두 일꾼이 채취할 수 있는 꿀의 최대 양은 C
초과하는 경우 두 통 중 하나마 채취할 수 있음

3.채취한 꿀은 시장에서 팔림
하나의 용기에 있는 꿀의 양이 많을수록 상품 가치가 높음
각 용기에 있는 꿀의 양의 제곱만큼 수익이 생김

입력
테스트 케이스 T
N(벌통들의 크기), M(벌통의 개수), C(꿀 채취할 수 있는 최대 양)

N*N개의 벌통에서 채취할 수 있는 꿀의 양에 대한 정보가 주어짐

"""
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 입력 받았음


    arr2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr[i][j] ** 2
    print(arr2)
    # 제곱한 값들을 저장한 리스트

    arr_TF = [[False] * N for _ in range(N)]  # False라면 양쪽을 더할 수 없음
    for i in range(N):
        for j in range(N-M+1):
            sum_honey = 0
            for m in range(M):
                sum_honey = arr[i][j+m]
            print(sum_honey)
            arr_TF[i][j] = (sum_honey <= C)
    print(arr_TF)

    arr_result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr_TF[i][j]:
                arr_result[i][j] = arr2[i][j] + arr2[i][j+1]
            else:
                arr_result[i][j] = arr2[i][j]

    max_idx = (0, 0)
    result = [0] * 2
    for rank in range(2):
        # second_result = 0
        for i in range(N):
            for j in range(N):
                if arr_result[i][j] > arr_result[max_idx[0]][max_idx[1]]:  # 제일 큰 값보다 크다면 갱신
                    max_idx = (i, j)
        result[rank] = arr_result[max_idx[0]][max_idx[1]]
        arr_result[max_idx[0]][max_idx[1]] = 0

                    # second_result = max_result
                    # max_result = arr_result[i][j]
                # elif arr_result[i][j] > second_result:  # 두번째로 큰 값보다 크다면 두번째 값만 갱신
                #     second_result = arr_result[i][j]



    print(arr_result)
    print(result[0], result[1])
    print(result[0] + result[1])