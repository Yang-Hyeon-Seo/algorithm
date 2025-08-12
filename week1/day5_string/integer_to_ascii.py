"""
양의 정수를 입력받아 문자열로 변환하는 함수 만들기
입력값 : 변환할 정수값, 변환된 문자열을 저장할 문자 배열
반환값 : 없음

아스키 표 보고 정수를 입력 받아서 문자열로 바꾸는 거(str()함수 사용x)
"""

import sys
sys.stdin = open("ascii_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    string = ''
    number = int(input())
    # 음수 여부 확인
    if number < 0:
        is_negative = True
        # 음수를 일단 양수로 바꾸기
        number *= -1
    else:
        is_negative = False
    # 1자리수만 만들 수 있으니까 자리수별로 계산해서 연결하기
    while number > 0:
        now_num = number % 10 # 현재 자릿수
        number = number // 10
        # ascii 에서 숫자가 48부터 시작함(0)
        string = chr(now_num + 48) + string  # chr 이 ascii 로 인식하는 함수인듯!

    if is_negative:
        string = '-' + string
    print(f'#{test_case} {string} {type(string)}')
