"""
1244_최대 상금_D3
주어진 숫자판 중 두개를 선택해서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있음
정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액 계산

음... 선택 정렬해서 제일 큰 수가 위로 올라가도록 하면 되는거 아님?
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    numbers, change_num = input().split()
    change_num = int(change_num)  # 숫자로 변환
    numbers = list(map(int, numbers))
    N = len(numbers)

    count = 0
    i = 0
    # print(numbers, change_num)

    while count < change_num and i < N:
        # 반복문 돌면서 앞에서부터 가장 큰 수로 채움
        max_idx = i  # 가장 큰 수 가리키는 인덱스
        max_number = 1  # 가장 큰수의 개수
        for j in range(i+1, N):  # 제일 앞에서 두번째 수부터 이용
            # 제일 큰 수 구하기
            # 제일 큰 수의 개수 구하기
            # 제일 큰 수의 개수만큼 앞에서 작은수부터 교환하기

            # 제일 큰 수 구하기
            if numbers[max_idx] < numbers[j]:
                # 제일 큰 수 갱신
                max_idx = j  # max_idx보다 큰 수라면 max_idx와 교환
                max_number = 1

            # 제일 큰 수의 개수 구하기
            elif numbers[max_idx] == numbers[j]:
                # 제일 큰 수 count + 1
                max_idx = j  # max_idx보다 큰 수라면 max_idx와 교환
                max_number += 1  #제일 큰 수 +1

        # print(numbers[i], numbers[max_idx])
        if numbers[i] != numbers[max_idx]:  # 자리 바꿔줘야 함
            check_number = min(max_number, change_num-count)
            min_number = i
            print(check_number, max_number, check_number-count)
            if check_number > 1:
                # 1이 넘는 경우에 자리 바꿀 대 신경을 써야 함

                for j in range(1, check_number):
                    # max_number와 change_num - count 중에 더 작은 수 만큼 반복해서 더 작은 수를 먼저 교환
                    if numbers[i+j] < numbers[min_number]:
                        min_number = i+j
                i -= check_number - 1

            numbers[min_number], numbers[max_idx] = numbers[max_idx], numbers[min_number]
            count += 1
            # print('교환', numbers, count)

        i += 1
        print(i, numbers, check_number, count)

    print(f'#{test_case} {"".join(map(str, numbers))}')