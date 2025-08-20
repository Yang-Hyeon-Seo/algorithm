class CircularQueue:
    # 큐 초기화 n개의 데이터 저장하기 위해 n+1 크기로 생성
    def __init__(self, n):
        self.capacity = n + 1  # 포화상태 구분을 위해 한 칸 비워둠
        self.items = [None] * self.capacity
        self.front = 0  # 큐의 시작 위치
        self.rear = 0  # 큐의 끝 위치

    def is_empty(self):
        """ 큐가 비어있는지 확인하는 메서드 """
        # front 와 rear 포인터가 같은 위치에 있으면 비어 있는 상태
        return self.front == self.rear

    def is_full(self):
        """ 큐가 가득 찼는지 확인하는 메서드 """
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        """ 큐의 rear에 데이터를 추가하는 메서드 """
        if self.is_full():
            # 큐가 가득찼다면 더 이상 추가할 수 없음
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        # 새로운 위치에 데이터 삽입
        self.items[self.rear] = item

    def dequeue(self):
        """ 큐의 front에서 데이터를 꺼내는 메서드 """
        if self.is_empty():
            # 큐가 비어있다면 꺼낼 데이터가 없음
            print("Queue is empty")
            return

        # front 포인터를 시계방향으로 한 칸 이동
        self.front = (self.front + 1) % self.capacity
        # 이동한 front 위치의 데이터 반환
        return self.items[self.front]


queue = CircularQueue(3)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
