"""
이왕이면 적을 때 *가 되고, 클 때 *를 피하는게 좋음
n-m의 값이 몇개인지(몇개를 틀렸는지)를 바탕으로
count가 k가 되는 순간에 틀리는 것으로 하고
곱해지는 것만 피하면 나머지는 언제 점수가 깎이는지 상관 없음
"""

import sys
sys.stdin = open('Sample_input.txt')
# sys.stdin = open('input.txt')


T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    counter_check = N//K  # 카운터가 들어가는 횟수 체크
    miss_check = N - M  # 틀린 개수 체크

    # print('counter_check', counter_check)
    # print('miss_check', miss_check)

    if counter_check <= miss_check:  # counter가 K가 되는 순간 항상 틀릴 수 있음 -> 맞춘 개수가 답
        # print('N-M이 N//K보다 많음', N, M, K)
        score = M
    else:
        # print('아님')

        # counter가 K가 되는 순간에 맞는 것들이 있음
        # 이 경우에 앞에서부터 맞추고, counter가 K가 되는 순간에 틀리면 됨
        score = 0
        counter = 0

        counter_number = counter_check - miss_check  # 카운터 맞춘 개수
        counter_list = []
        for i in range(1, counter_number + 1):
            # print(i)
            counter_list.append(K * i)

        # print(score, counter)
        # print('counter_number', counter_number)
        # print(counter_list)

        for i in range(1, N+1):
            # 맞출 카운터에 해당하는 경우
            if i in counter_list:
                score += 1
                score *= 2
                counter = 0
            elif counter+1 != K:  # 카운터가 아닐 땐 score에 1을 더함, counter도 1을 올려줌
                score += 1
                counter += 1
            else:  # counter_list에 들어 있지 않으면서 counter가 K가 되는 순간에
                counter = 0
            # print(score, counter, i)

            # miss_counter = counter_check - miss_check  # 이 값이 counter 안에 몇개가 틀릴지 의미
            # -> 이거 만큼 뒤에서부터
            # counter_check - miss_counter = 카운터 맞춘 개수
            # 정답을 맞춘 카운터 인덱스를 리스트로 만들어서 i가 해당 인덱스가 되면 score + 1, score * 2, counter = 0
            # 순서대로 진행
            # 맞출 카운터 인덱스는 알 수 있음(앞에서부터 맞출거니까)
            #if i ==
    print(f'#{test_case} {score}')