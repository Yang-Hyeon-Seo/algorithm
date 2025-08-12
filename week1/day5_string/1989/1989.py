"""
level 과 같이 거꾸로 읽어도 제대로 읽은 것고 같은 문장이나 낱말을 회문이라고 함
단어를 입력받아 회문이면 1을 출력하고 아니면 0을 출력하는 프로그램을 작성
"""

import sys

# 회문을 확인하는 함수
def is_palindrome(string):
    """
    string 이 거꾸로 읽어도 제대로 읽은 것과 같은지 확인하는 함수
    동일하다면 1, 그렇지 않다면 0을 리턴함
    """
    reversed_string = []
    for idx in range(len(string)-1, -1, -1):  # 문자열을 거꾸로 돌면서 append
        reversed_string.append(string[idx])

    # 문자열 동일한지 검사
    if ''.join(reversed_string) == string:
        return 1
    else:
        return 0


# 입력받기
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # 문자열 입력 받음
    string = input()
    # 문자열 검사한 결과 출력
    print(f'#{test_case} {is_palindrome(string)}')