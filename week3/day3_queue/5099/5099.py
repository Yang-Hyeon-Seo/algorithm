"""
5099_피자굽기_D3
N개의 피자를 동시에 구울 수 있는 화덕이 있음
피자는 치즈가 모두 녹으면 화덕에서 꺼냄
치즈의 양은 피자마다 다름
1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣음
치즈의 양에 따라 노는 시간이 다르기 때문에 꺼내지는 순서는 달라질 수 있음
화덕에 가장 마지막에 남아 있는 피자 번호 알아내기
"""
from collections import deque
import sys
sys.stdin = open('sample_input.txt')


def check_pizza():
    """
    피자 나오는거 하려고 하는데 잘 모르겠음
    :return:
    """
    pass

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    count = [0] * M

    # //2를 몇번씩 해야 하는지 확인
    for i in range(M):
        while arr[i] != 0:
            count[i] += 1
            arr[i] = arr[i] // 2
            # print('count', count)
            # print('arr', arr)
    print(count)
    # count 리스트 안에서 숫자가 가장 큰 것 중에서 인덱스 가장 큰 것 찾기
    if N > M:  # 화덕 한 번에 다 들어가는 경우
        max_count = 0
        result = 0
        for i in range(M):
            if count[i] >= max_count:
                max_count = count[i]
                result = i
    else:
        # 화덕 한 번에 다 안 들어가는 경우
        fire_count = [[0, 0] for i in range(N)]  # [피자 번호-1, 치즈녹는데걸리는수]
        # 처음에 화덕에 들어가야 하는 것들 다 넣고
        for j in range(N, M):
            for i in range(N):
                fire_count[i] = [i, count[i]]
            min_num = fire_count[1]
            min_idx = fire_count[0]
            for i in range(1, N):
                if fire_count[i][1] < min_num:
                    min_num = fire_count[i][1]
                    min_idx = i
            # 가장 작은거 찾아서 그만큼 빼고 그 위치에 피자 넣기
            for i in range(N):
                fire_count[i][1] = fire_count[i][1] - min_num
            fire_count[i] = [j, count[j]]
    # 누구 하나 빠지면 다음 들어갈 거임
            # 빠진 위치에 새로 들어감




    # 결과 출력
    print(f'#{test_case} {result + 1}')

    # # 큐 안에 들어간 형태 [치즈, 번호]
    #
    # queue = deque()
    # # print(len(queue))
    # idx = 0  # 현재 인덱스 위치  (피자의 인덱스 출력할 때 + 1 해줘야함
    # if N > M:  # 화덕에 다 넣을 수 있음
    #     for i in range(M):  # 큐에 피자 넣기
    #         queue.append([arr[i], i])  # 0~(M-1)번의 피자를 넣음
    #     idx = M - 1
    #
    #     # 화덕 돌면서 가장 늦게 나오는거 찾기
    #
    # else:
    #     for i in range(N):
    #         queue.append(([arr[i], i]))
    #     idx = N - 1
    # # print(len(queue))
    #
    #     while idx < M and len(queue) > 0 : # idx가 N 보다 작고, 큐가 비어있지 않은 동안 반복
    #         while True:  # break문을 만날 때까지 반복
    #             print(queue)
    #             cheese, pizza = queue.popleft()  # 화덕에서 꺼냄
    #             cheese = cheese // 2  # 치즈가 반으로 줄었음
    #             if cheese == 0:
    #                 print('녹음')
    #                 result = pizza + 1
    #                 break  # 치즈가 0이면 break를 함함    # idx가 N 이상이 되거나 queue의 길이가 0이 되면 반복 종료
    #             else:
    #                 queue.append([cheese, pizza])
    #                 print('아직 안녹음') # , queue)
    #         # 추가가 될 타이밍이면
    #         idx += 1  # 화덕에서 하나 빼면 하나 추가함
    #         queue.append([arr[idx], idx])
    #         print("추가", queue)
    #     print(queue)
    #     print(f'#{test_case} {result}')
    #
    #
    #
    #
    #
    # # 갑자기 드는 생각인데 치즉가 몇 바퀴 돌았을때 0이 되는지 파악해서 해도 되지 않을까