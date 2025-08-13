"""
16504_gravity (D2)
가로 N 세로 100 크기의 방에 상자들이 쌓여 있음
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때
가장 큰 낙차 구하기
"""

import sys
sys.stdin = open('in.txt')


# 정렬 여부 확인 함수
def check_sorted(arr, N):
    """
    정렬 여부 확인하는 함수
    오름차순 정렬이기 때문에 만약 더 작은 인덱스의 값이 더 크다면 정렬되지 않은 것임
    :param arr: 정렬할 인덱스
    :param N: arr의 길이
    :return: 정렬 여부 부울형으로 반환
    """
    for i in range(N-1):
        if arr[i] > arr[i+1]:
            # 정렬되지 않았으면
            return False
    return True



# 뒤에서부터 정렬하는 함수(count + 1하기)
def sort_count(arr, N):
    """
    재귀함수 사용해보기
    :param arr:
    :param N:
    :return:
    """

    if check_sorted(arr, N):  # 정렬되어 있다면
        # print(arr)
        return 0
    else:  # 정렬되어 있지 않다면
        # 뒤에서부터 정렬하고 해당 arr로 재귀호출하는데 count 반환하니까 +1하기
        for i in range(N-2, -1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        # print(arr)
        return sort_count(arr, N) + 1



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 가로 길이
    arr = list(map(int, input().split()))  # 상자가 쌓여 있는 형태
    # 입력 확인
    # print(arr)
    count = sort_count(arr, N)

    print(f'#{test_case} {count}')
