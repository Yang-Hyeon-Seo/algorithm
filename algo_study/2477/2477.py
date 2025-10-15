import sys
sys.stdin = open('sample_input.txt')

from collections import deque


def N_is_empty(N, left_a_time):
    for i in range(1, N+1):
        if left_a_time[i][0] != 0:
            return False
    return True

T = int(input())
for test_case in range(1, T+1):
    N, M, K, target_N, target_M = map(int, input().split())
    ai = [0] + list(map(int, input().split())) # 접수창구는 1번부터 시작함, 0번 인덱스는 버림
    bi = [0] + list(map(int, input().split())) # 정비창구도 1번부터 시작
    t = [0] + list(map(int, input().split()))  # 고객 방문 시간, 고객 번호도 1번부터 시작

    result = [[0, 0] for i in range(K+1)]  # 고객 번호도 1번부터 시작함, 0번 인덱스는 버리고, 인덱스는 K까지 있음
    left_a_time = [[0, 0] for _ in range(N + 1)]  # 접수 창구의 남은 수행 시간
    left_b_time = [0] * (M + 1)  # 정비 창구의 남은 수행 시간

    # print(N, M, K, target_N, target_M)
    # print(ai)
    # print(bi)
    # print(t)
    # print(result)
    # print(left_a_time)
    # print(left_b_time)

    que1 = deque()  # 접수 창구 대기 줄
    que2 = deque()  # 정비 창구 대기 줄

    #for time in range(t[0], t[-1]):  # 1시간마다 갱신할거임
    time = t[1]
    while True:
        # print('현재시간', time)
        # 고객 처리 로직
        for i in range(1, N + 1):
            if left_a_time[i][0] > 0:
                left_a_time[i][0] -= 1
                if left_a_time[i][0] == 0:
                    que2.append(left_a_time[i][1])
                    left_a_time[i][1] = 0  # 자리도 비워준다
        for j in range(1, M + 1):
            if left_b_time[j] > 0:
                left_b_time[j] -= 1

        # print('창구 상황')
        # print(left_a_time)
        # print(left_b_time)
        # print('대기줄상황')
        # print(que1)
        # print(que2)
        #
        # print('고객 입장')

        # 고객 받는 로직
        for customer in range(1, K+1):
            if t[customer] == time:
                # print(customer, '번 고객 방문')
                que1.append(customer)
            elif t[customer] > time:
                # print(customer, '번 이후부터는 아직 방문 X')
                break  # 아직 고객이 도착하지 않음
            # 나머지는 이미 확인했음

        # print('접수 창구 배정', que1)

        # 접수 창구 배정 로직
        for i in range(1, N+1):
            if left_a_time[i][0] == 0 and len(que1) > 0:
                customer = que1.popleft()
                result[customer][0] = i  # result에 기록
                left_a_time[i] = [ai[i], customer]  # 남은 시간 갱신
                # print(customer, '번 고객', i, '번 접수 창구 배정', left_a_time[i], '시간 남음')

        # print('정비 창구 배정', que2)

        # 정비 창구 배정 로직
        for j in range(1, M+1):
            if left_b_time[j] == 0 and len(que2) > 0:  # 창구가 비어 있다면
                customer = que2.popleft()
                result[customer][1] = j
                left_b_time[j] = bi[j]
                # print(customer, '번 고객', j, '번 접수 창구 배정', left_b_time[j], '시간 남음')


        time += 1
        if time > t[-1] and len(que1) <= 0 and len(que2) <= 0 and N_is_empty(N, left_a_time):
            # print(time, len(que1), len(que2), left_a_time)
            break
        # print('시간 경과')


    # print(result)
    count = 0
    for i in range(1, K+1):
        if result[i] == [target_N, target_M]:
            # print(i, result[i])
            count += i
    if count == 0:
        count = -1
    print(f'#{test_case} {count}')

    # print('---------------------------------')