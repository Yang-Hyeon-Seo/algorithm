"""
1860_진기의최고급붕어빵
붕어빵을 보통 사람들에게 팔지 않음
무조건 예약제로 손님을 받고, 예약하려는 손님들은 진기의 까다로운 자격 검증에서 합격해야 함
N명의 사람이 자격을 얻음
0초부터 M초 시간을 들이면 K개의 붕어빵을 만들 수 있음
지연시간 없이 다른 붕어빵 만들 수 있음
0초 이후에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 기다리는 시간 없이 붕어빵을 제공할 수 있는지 판별하는 프로그램 작성

첫 번째 줄에 테스트케이스 수 T가 주어짐
각 테스트케이스 첫번째 줄에는 N, M, K가 공백으로 구분되어 주어짐
(1 <= N, M, K <= 100)
두번째 줄에는 N개의 정수가 공백으로 구분되어 주어짐
각 정수는 각 사람이 언제 도착하는지를 초단위로 나타냄

붕어빵을 제공할 수 있으면 Possible, 제공할 수 없으면 Impossible 출력
"""

import sys
sys.stdin = open('input.txt')


# 오름차순 정렬
# 오랜만에 카운팅 정렬 연습
def counting_sort(arr, N):
    """
    카운팅 정렬
    :param arr: 정렬할 리스트
    :param N: 리스트의 길이
    :return: 정렬된 리스트
    """
    # arr의 가장 큰 값 찾기
    max_idx = 0  # arr의 첫번째 값을 max_num으로 넣음
    for i in range(1, N):  # 첫 번째 값은 검사 안 해도 됨
        if arr[i] > arr[max_idx]:
            max_idx = i

    counts = [0] * (arr[max_idx] + 1)
    sorted_list = [0] * N

    # arr 돌면서 counts 계산하기
    for i in range(N):
        counts[arr[i]] += 1

    # 누적합 만들기
    for i in range(1, arr[max_idx]+1):
        counts[i] += counts[i-1]

    # 정렬하기
    for i in range(N-1, -1, -1):  # 마지막 값까지 돌아야 함(그래야 마지막까지 정렬되니까)
        counts[arr[i]] -= 1
        sorted_list[counts[arr[i]]] = arr[i]

    return sorted_list



T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())  # M 초 시간을 들이면 K 개 붕어빵을 만들 수 있음
    arr = list(map(int, input().split()))  # 리스트의 길이는 N
    fish = 0  # 붕어빵의 수

    # 사람들의 도착 시간을 오름차순으로 정렬
    arr = counting_sort(arr, N)
    # print(arr)

    # for 돌면서 arr[i]//M * K 한 값 1 빼고 만약 음수가 되면 fail
    for i in range(N):
        # print(arr[i], '초', ((arr[i] // M) * K) - i)
        # print(arr[i], arr[i]//M, arr[i]//M*K-i-1)
        if arr[i] // M * K - i - 1 < 0:
            # arr[i] : 고객이 온 시간
            # 그 시간동안 만들 수 있는 붕어빵의 수는 arr[i]//M*K
            # 그 시간동안 온 손님의 수 : i + 1
            # arr[i]//M*K - (i+1)
            print(f'#{test_case} Impossible')
            break
    else:
        print(f'#{test_case} Possible')
