'''
0~9까지 적힌 N장의 카드에서 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(T):
    # 버블소트 사용하기
    N = int(input())
    numbers = list(map(int, input()))
    #print(numbers)

    # 버블소트
    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(numbers)

    # 리스트 돌면서 같은 것 나오면 +1
    max_number_count = [0, 0] # 번호, 횟수
    count = 0
    # 다른것 나오면 지금까지의 수랑 최대 카운트랑 비교해서
    for i in range(N):
        if count == 0: # 처음 시작이면
            max_number_count[0] = numbers[i] # 첫번째 값 넣기
            count = 1 # 카운트 1 늘리기
            continue
        if numbers[i] == max_number_count[0]: # 값이 같으면
            count += 1
        else: # 값이 다르면
            if max_number_count[1] <= count: # count가 더 크면
                max_number_count[0] = numbers[i]
                max_number_count[1] = count
                count = 1
            else:
                count = 1
    # 마지막 수가 제대로 반영되지 않음
    if max_number_count[1] <= count:  # count가 더 크면
        max_number_count[0] = numbers[i]
        max_number_count[1] = count
    print(f'#{test_case} {max_number_count[0]} {max_number_count[1]}')



    # # bubble sort 말고 다른 방법
    # N = int(input())
    # arr = [0]*10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # # 인덱스가 카드 번호
    # # 카드 번호에 해당하는 인덱스를 1 늘리기
    # # arr[카드번호] = 해당 번호가 적힌 카드 수
    # numbers = input()
    # for number in numbers:
    #     num = int(number)
    #     arr[num] += 1
    #
    # # 값이 가장 큰 수와 인덱스 찾기
    # max_idx = 0 # 가장 큰 수를 0번째 인덱스라고 가정
    # for i in range(1, len(arr)):
    #     if arr[i] >= arr[max_idx]:
    #         max_idx = i # 인덱스 바꾸기
    #
    # print(f'#{test_case} {max_idx} {arr[max_idx]}')
