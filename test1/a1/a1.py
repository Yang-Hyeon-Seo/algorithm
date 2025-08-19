import sys
# sys.stdin = open('sample_input.txt')
sys.stdin = open('input.txt')


def is_not_all_0 (arr, N):
    for i in range(N):
        if arr[i] != 0:  # 0이 아닌 것이 있으면 True 리턴
            return True
    return False  # 모두 0이라면 False 리턴


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 가장 높이가 큰 수 찾기
    max_height = arr[0]
    for i in range(1, N):
        if max_height < arr[i]:
            max_height = arr[i]
    # print(max_height)

    # 차이 계산하기
    arr_need = [0] * N  # 성장이 필요한 양을 나타냄(need)
    for i in range(N):
        arr_need[i] = max_height - arr[i]
    arr_need.sort()
    # print(arr_need)


    day = 0
    while is_not_all_0 (arr_need, N): # 차이 계산해서 모두 0인지 아닌지 확인하는 함수
        day += 1  # 다음날로 이동
        for i in range(N):  # 모든 수에 대해
            if arr_need[i] == 0:
                # 이미 최대로 성장함
                continue
            # 각 차이가 1이면 홀수인 날에 물을 줌 (짝수 건너뜀)
            elif arr_need[i] == 1:
                if day % 2 == 1:  # 홀수인 날
                    arr_need[i] -= 1
                    break  # 하루에 나무 1개만 물을 줄 수 있으므로 arr_need 순회 중지
                else:             # 짝수인 날
                    continue
            # 각 차이가 2이면 짝수인 날에 물을 줌
            elif arr_need[i] == 2:
                if day % 2 == 1:  # 홀수인 날
                    continue
                else:             # 짝수인 날
                    arr_need[i] -= 2
                    break  # 하루에 나무 1개만 물을 줄 수 있으므로 arr_need 순회 중지
            # 각 차이가 3 이상인 경우 계속 물을 줌
            else:  # arr_need[i] >= 3
                if day % 2 == 1:  # 홀수인 날
                    arr_need[i] -= 1
                    break  # 하루에 나무 1개만 물을 줄 수 있으므로 arr_need 순회 중지
                else:             # 짝수인 날
                    arr_need[i] -= 2
                    break  # 하루에 나무 1개만 물을 줄 수 있으므로 arr_need 순회 중지

        # print(day, arr_need)
    print(f'#{test_case} {day}')

    # while # 모든 차이가 0이 아닌 동안 반복 (하나라도 0이 아닌 것이 있으면 반복)
