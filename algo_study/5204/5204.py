"""
5204_병합정렬

"""

import sys
sys.stdin = open('sample_input.txt')


def merge(left_arr, right_arr):
    merged_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_arr]
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

    # 남은것들 그냥 붙여주기
    merged_arr.extend(left_arr[left_idx:])
    merged_arr.extend(right_arr[right_idx:])
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 분할
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 정복
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 통합
    return merge(left_sorted, right_sorted)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)