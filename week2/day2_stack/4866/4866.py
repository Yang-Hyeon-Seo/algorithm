"""
주어진 입력에서 {}와 ()가 제대로 짝을 이뤘는지 검사하는 프로그램 만들기
제대로 짝을 이룬 경우 1, 그렇지 않으면 0
"""

import sys
sys.stdin = open(('sample_input.txt'))

T = int(input())
for test_case in range(1, T + 1):
    code = input()
    N = 100  # 리스트 길이 -> 필요한 건 아니지만, 나중에 리스트의 길이를 수정하기 쉽게 만들어 봄
    stack = [0] * N  # 길이가 정해진 스택 만들기
    top = -1  # 스택의 top 가리킬 포인터
    result = 1  # 결과값 저장할 변수 / 일단 문제가 없음

    for i in code:
        # code 순회하면서 값을 확인
        # print(i)

        # 열린 괄호가 나오면 스택에 추가
        if i in ['(', '{']:
            # top 이미 스택의 제일 위를 가리키고 있다면 overflow
            if top == N - 1:
                result = -1  # 오버플로우
                break
            # 스택 제일 위를 가리키고 있지 않다면
            else:
                top += 1
                stack[top] = i

        # 닫힌 괄호가 나오면 스택의 값 확인해서 짝꿍이면 pop 짝꿍이 아니면 0저장
        elif i in [')', '}']:
            if top == -1:  # 빈 리스트 -> 짝이 안 맞음
                result = 0
                break
            else:
                if stack[top] == '(' and i == ')':  # 만약 마지막에 쌓인게 열린 소괄호 & 이번 값이 닫힌 소괄호
                    top -= 1
                elif stack[top] == '{' and i == '}':
                    top -= 1
                else:  # 짝이 안 맞는 경우
                    result = 0
        # 다른 문자가 나오는 경우 -> 아무것도 하지 않음
    # 다 돌았는데 괄호가 남아 있는 경우 -> 짝이 안 맞음
    if top != -1:  # top -1이 아니면 -> 값이 남아 있음
        result = 0

    print(f'#{test_case} {result}')