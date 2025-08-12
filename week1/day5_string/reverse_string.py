"""
연습문제1 - 문자열 뒤집기

자기 문자열에서 뒤집는 방법이 있고, 새로운 빈 문자열 만들어 소스의 뒤부터 읽는 방법이 있음
- 자기 문자열을 이용할 경우, swap을 위한 임시 변수 필요, 반복 수행을 문자열 길이의 반만큼
"""

# 입력
import sys
sys.stdin = open('input_reverse_string.txt')

T = int(input())
for test_case in range(1, T + 1):

    # 새로운 빈 문자열 만들어서 뒤집는 방법
    string = input()
    reversed_string = []

    for i in range(len(string)-1, -1, -1):
        reversed_string.append(string[i])

    # 출력
    print(f'# {test_case}{"".join(reversed_string)}')

    # 자기 문자열에서 뒤집는 방법
    """
    len(string)의 절반만 회전
    9//2 = 4 -> range(4) 하면 앞부분 기준 4 바로 앞까지 반복    
    10//2 = 5 --> 0~4까지 반복하는데 0~4, 5~9 바꾸면 됨
    """
    # str은 내용을 바꿀 수 없음 -> 리스트로 만들기
    string = list(input())

    length = len(string)
    for i in range(length // 2):
        string[i], string[length-i-1] = string[length-i-1], string[i]

    # 출력
    print(f'# {test_case}{"".join(string)}')