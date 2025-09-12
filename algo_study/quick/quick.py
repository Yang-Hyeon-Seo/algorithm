"""
배열의 데이터를 퀵 정렬하는 함수 작성 및 테스트

"""
import sys
sys.stdin = open('input.txt')


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        # 분할
        pivot_idx = partition(arr, start, end)

        # 정복
        # 왼쪽 부분
        quick_sort(arr, start, pivot_idx - 1)
        # 오른쪽 부분
        quick_sort(arr, pivot_idx + 1, end)




T=int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr)-1)

    print(f'#{test_case} {" ".join(map(str, arr))}')