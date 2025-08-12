"""
문자열 s에서 반복되는 문자 지우려고 함
지워진 부분은 다시 앞, 뒤를 연결함
만약 연결에 의해 또 반복문자가 생기면 이 부분을 다시 지움
반복 문자를 지운 후 남은 문자열의 길이 출력하기

동일한 문자 2개가 연달아서 나옴 -> 2개 빼고 나머지만 연결

문자 지울 때 처음부터 할 필요는 없을듯!
지운 문자 1칸 앞부터 다시 점검해서 만약 동일한 문자라면 지우는 것으로 하기

앞에서부터 문자 1개씩 넣으면서 바로 앞 문자랑 비교하기
비교해서 동일한 문자면 pop하면서 빼고, 다음 문자로 넘어가기
마지막에 top 포인터의 위치로 파악하기

클래스로 만들어보기
"""

import sys
sys.stdin = open('sample_input.txt')


class Stack:
    def __init__(self, size):
        self.size = size
        self.capacity = [0] * size
        self.top = -1
    def push(self, item):
        if self.top == self.size - 1:  # top 제일 위 가리킨다면
            return 'oveflow'
        else:
            self.top += 1
            self.capacity[self.top] = item
            return 'done'

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():  # 스택이 비어 있는 경우
            return 'underflow'
        else:
            self.top -= 1
            return self.capacity[self.top + 1]

    def peek(self):
        if self.top == -1:  # 스택이 비어 있는 경우
            return 'empty'
        return self.capacity[self.top]

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    stack = Stack(len(string))

    for s in string:
        # print(s, stack.capacity)
        if s == stack.peek():  # 제일 위 값이랑 같다면
            stack.pop()  # 제일 위의 값 빼고 다음값으로 넘어감
            continue
        else:  # 다르다면
            stack.push(s)
        # print(stack.capacity)

    # 남은 문자열 길이 확인하기
    result = stack.top + 1
    print(f'#{test_case} {result}')