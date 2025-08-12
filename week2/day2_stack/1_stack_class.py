class Stack:
    def __init__(self, size):
        self.top = -1
        self.capacity = [0]*size
        self.size = size

    def push(self, item):
        if self.top == self.size - 1:  # top이 가리키는 곳이 size의 제일 마지막 원소인지 확인
            # 만약 그렇다면
            return "Oveflow"
        else:
            # 아니라면
            self.top += 1  # top 1개 늘리고
            self.capacity[self.top] = item  # 그 위치에 item 저장

    def pop(self):
        if self.top == -1 :  # 비어있는 리스트라면
            return "Underflow"
        else:
            # 아니라면
            self.top -= 1
            return self.capacity[self.top + 1]

stack = Stack(3)
for i in range(3):
    stack.push(i)
for i in range(3):
    print(stack.pop())