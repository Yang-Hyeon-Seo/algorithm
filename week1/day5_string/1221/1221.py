"""
0~9의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정려하여 출력하는 프로그램
'ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'
문자열을 받아 정렬해서 다시 출력
"""
# 아이디어
"""
원래 딕셔너리 쓰려고 했는데, 영어 -> 숫자 또는 숫자 -> 영어는 ok지만 반대가 조금 곤란함
카운트정렬하듯이 리스트 1개 이용

출력 신경쓰기
"""

import sys

sys.stdin = open("GNS_test_input.txt")

# 우리와 다른 숫자체계를 가진 행성의 0~9값
numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for test_case in range(1, T + 1):
    # 입력 받기
    input_test_case, input_length = input().split()
    length = int(input_length)
    input_numbers = list(input().split())
    counts = [0] * 10  # 카운팅 정렬 처럼
    int_list = [0] * length   # 입력받은 값들을 숫자로 변환한 값을 갖는 리스트

    # 영어 -> 숫자로
    for i in range(length):
        for j in range(10):  # len(numbers)
            if input_numbers[i] == numbers[j]:
                counts[j] += 1
    # 누적합
    for i in range(1, 10):
        counts[i] += counts[i-1]
    #print(counts)
    # 정렬, 숫자 -> 영어로
    for i in range(length-1, -1, -1):
        for j in range(10):  # len(numbers)
            if input_numbers[i] == numbers[j]:
                counts[j] -= 1  # 하나 빼고
                int_list[counts[j]] = numbers[j]
                break

    # 출력
    print(input_test_case, ' '.join(int_list))