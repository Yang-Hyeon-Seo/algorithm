"""
5097_회전_D2
N개의 숫자로 이루어진 수열이 존재함
맨 앞의 순자를 맨 뒤로 보내는 작업을 M번 했을 떄 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만들기
"""

# 아이디어
"""
Circular Queue 만들면 될듯!
"""

class CircularQueue:
    def __init__(self, n):
        self.capacity = n+1  # n 개의 데이터 -> 다 찼을때와 구분하기 위해 n+1 사용
        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        """
        비어 있는지 확인하는 함수
        """
        return self.front == self.rear  # front와 rear가 같이 있다면 비어있음 -> True 리턴

    def is_full(self):
        """
        다 찼는지 확인하는 함수
        """
        return self.front == (self.rear) % self.capacity  # rear에 1 더하고 길이만큼 나눈 나머지가 front와 같으면 다 참
        # 이렇게 생긴거임
        """
        [_, _, _, r, f, _, _] -> r + 1하면 f랑 같아짐
        또는
        [f, _, _, _, _, _, r] -> (r+1) % capacity 하면 f랑 같아짐
        """

    def enqueue(self, n):
        if self.is_full():
            # 다 찼으면 enque 불가능
            print('불가능!')
            return None
        # 다 안찼다면
        self.rear += 1
        self.items[self.rear] = n
        return None

    def dequeue(self):
        if self.is_empty():
            # 비어있다면 deque 불가능
            print('불가능!!')
            return None
        # 비어있지 않다면
        self.front += 1
        return self.items.pop(self.front)


import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(N, M, arr)
    queue = CircularQueue(N)
    for i in range(N):
        queue.enqueue(arr[i])
    print(queue)
    for i in range(M):
        tmp = queue.dequeue()
        queue.enqueue(tmp)

    print(f'#{test_case} {queue.dequeue()}')




    #