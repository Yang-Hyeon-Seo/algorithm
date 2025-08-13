"""
1215_회문1
회문 : palindrome이라고 함
8x8 평면 글자판에서 제시된 회문의 개수 구하기
칸에 들어가는 글자는 'A', 'B', 'C' 중 하나임
ABA, ABBA, A 모두 회문임
가로 또는 세로로 이어진 회문의 개수만 셈

찾아야 하는 회문의 길이(N) 제공

회문 찾는 함수 만들어서 진행
회문 찾는 함수를 2번 사용할건데, 1번은 그냥 arr을 사용하고,
2번째는 오른쪽으로 90도 돌린 arr을 사용할 것
(이렇게 하는 경우 함수를 재사용할 수 있기 때문에)
"""

import sys
sys.stdin = open('input.txt')


# 회문인지 아닌지 파악하는 함수
def is_palindrome(string, length):
    """
    회문인지 아닌지 파악하는 함수
    :param string: 확인할 문자열
    :param length: 문자열의 길이
    :return: 회문이면 1, 아니면 0
    """
    # print(string)
    for i in range(length//2):
        if string[i] != string[length-i-1]:  # 회문이 아님
            return 0
    return 1


# 회문 찾는 함수
def fine_palindrome(arr, length):
    """
    회문 찾는 함수
    :param arr: 회문을 찾을 문자판
    :param length: 회문의 길이 (길이 N짜리의 회문 찾기)
    :return: 회문의 길이 리턴
    """
    count = 0  # 회문의 개수 찾는 변수
    N = len(arr)  # 문자판의 크기 (여기에서는 8, 만약 글자판의 길이도 변수로 준다면? 이라는 생각으로 N으로 만들어봤음)
    
    for i in range(N):
        # print(i)
        for j in range(N - length + 1):
            # 행 우선 순회, length 확인할만큼 여유 공간 남겨놓기
            # 행 순회하면서 회문이 있는지 확인
            count += is_palindrome(arr[i][j:j+length], length)
            # print(arr[i][j:j+length], is_palindrome(arr[i][j:j+length], length), length, count)
    return count


T = 10  # 테스트 케이스의 개수는 10
for test_case in range(1, T + 1):
    N = int(input())  # 회문의 길이
    arr = [input() for _ in range(8)]  # 8x8 글자판이기 때문에 8번 반복

    count = fine_palindrome(arr, N)

    # 오른쪽으로 90도 회전
    rotated_arr = list(map(list, zip(*arr[::-1])))
    # print(rotated_arr)
    count += fine_palindrome(rotated_arr, N)

    print(f'#{test_case} {count}')
