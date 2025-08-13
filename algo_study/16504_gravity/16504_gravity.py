"""
16504_gravity (D2)
가로 N 세로 100 크기의 방에 상자들이 쌓여 있음
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때
가장 큰 낙차 구하기
"""
import copy

import sys
sys.stdin = open('in.txt')


def selection_sort_drop_count(arr, N):
    """
    선택정렬

    새로운 리스트 만들어서
    새로운 리스트의 뒤에서부터 가장 큰 값(가장 뒤에 있는)부터 넣는데
    기존 리스트의 인덱스에서 얼마나 이동하게 되었는지를 max_num과 비교해서
    만약 max_drop보다 크면 max_drop 갱신하고, 아니면 그냥 날리기

    :param arr: 정렬할 리스트
    :param N: 리스트의 길이
    :return: 정렬된 리스트
    """

    sorted_arr = copy.copy(arr)  # 중첩 리스트가 아니니까 그냥 copy하면 됨
    # sorted_arr = arr[:]  # 이것도 동일함
    max_drop = 0  # drop
    for i in range(N-1, 0, -1):  # 뒤에서부터 돌면서 체크
        max_idx = i
        for j in range(1, i):
            if arr[j] >= arr[max_idx]:
                max_idx = j
        drop = i - max_idx
        if max_drop < drop:
            max_drop = drop


    return max_drop



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 가로 길이
    arr = list(map(int, input().split()))  # 상자가 쌓여 있는 형태
    # 입력 확인
    # print(arr)

    # 이거 그냥 정렬하면 되는거 아님?
    # (떨어지면서 넘치는 부분이 아래로 이동하면서 높이는 똑같은데 정렬되는 효과가 있으니까)
    # 버블소트로 이동하는 양을 계산할까? -> 가장 마지막까지 이동하는 해당 줄에서 낙차가 가장 큰거니까

    # 선택정렬
    max_drop = selection_sort_drop_count(arr, N)

    print(f'#{test_case} {max_drop}')
