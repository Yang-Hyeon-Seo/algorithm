'''
N 길이의 숫자열을 오름차순으로 정렬하여 출력
'''

# 입력받기
import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 선택정렬
    for i in range(N):
        # 가장 작은 것 탐색
        min_idx = i #가장 작은 인덱스에 현재 인덱스 할당
        for j in range(i + 1, N): # i + 1부터 돌면서 가장 작은 값 찾기
            if arr[j] < arr[min_idx]:
                min_idx = j # 가장 작은 수 인덱스 수정
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


    # 버블정렬
    for i in range(N-1, -1, -1): # 뒤에서부터 정렬
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    # 출력
    print(f'#{test_case}', end=' ')
    for i in range(N):
        print(arr[i], end=' ')
    print()


    # 카운팅 정렬
    # 가장 큰 수 찾기
    max_num = 0
    for i in range(N):
        if arr[i] > max_num:
            max_num = arr[i]
    # 정렬된 리스트 만들기
    sorted_list = [0] * N # 이거 만드는 것을 잊고 있어서 문제가 안풀렸음,,!!

    # counts 리스트 만들기
    counts = [0] * (max_num + 1)

    # counts 카운트하기
    for i in arr:
        counts[i] += 1

    # 누적합 만들기
    for i in range(1, max_num+1):
        counts[i] += counts[i-1]
    #print(counts)

    # arr의 가장 뒤에서부터 정렬하기
    for i in range(N-1, -1, -1):
        counts[arr[i]] -= 1
        sorted_list[counts[arr[i]]] = arr[i]


    # 출력
    print(f'#{test_case}', end=' ')
    for i in range(N):
        print(sorted_list[i], end=' ')
    print()





