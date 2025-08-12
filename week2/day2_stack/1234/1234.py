"""
1234_비밀번호
0~9로 이루어진 번호 문자열에서 같은 번호로 붙어 있는 쌍들을 소거하고 남은 번호들 비밀 번호로 만듦
번호 쌍이 소거되고 소거된 번화 쌍의 좌우 번호가 같은 번호면 소거

"""

import sys
sys.stdin = open('input.txt')


class Stack:
    def __init__(self, size):
        self.size = size
        self.capacity = [0] * size
        self.top = -1

    def push(self, item):
        # 만약 top이 이미 꼭대기를 가리키고 있다면
        if self.top == self.size - 1:
            return 'overflow'
        else:
            self.top += 1
            self.capacity[self.top] = item

    def is_empty(self):
        return self.top == -1  # -1이라면 빈 스택

    def pop(self):
        if self.is_empty():  # 비어있다면
            return 'underflow'
        else:
            self.top -= 1
            return self.capacity[self.top + 1]

    def peek(self):
        if self.is_empty():
            return 'empty'
        else:
            return self.capacity[self.top]

    def print(self):
        for i in range(self.top + 1):
            print(i, end='')


T = 10
for test_case in range(1, T + 10):
    N, numbers = input().split()
    N = int(N)

    stack = Stack(N)

    for number in numbers:
        # 지금 넣으려는 값이 스택의 제일 위에 있는 경우, 넣지 않고, 스택 제일 위의 값도 뺌
        if stack.peek() == number:
            # 스택 제일 위에 있는 경우
            stack.pop()
        else:
            # 스택 제일 위에 없는 경우
            stack.push(number)
    print(f"#{test_case}", end=' ')
    stack.print()
    print()