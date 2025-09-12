"""
n개의 수를 처리하면 8자리의 암호를 생성할 수 있음
- 8개의 숫자를 입력 받음
첫번째 숫자를 1 감소하고 맨 뒤로 보냄

다시 첫번째 수를 2 감소하고 맨 뒤로 보냄

다시 첫번쨰 수를 3 감소하고 맨 뒤로 보냄

5까지 줄이고 맨 뒤로 보냄
- 이게 한 사이클임
숫자가 감소할 때 0보다 작아지면 0으로 유지되며 프로그램이 종료됨
이때 8자리 숫자값이 암호가 됨

=> 감소했을 때 0보다 작아지면, 그 수를 제일 뒤로 보내서 마지막은 0이 되고, 문제가 끝남
"""

import sys
from collections import deque

sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    test_number = int(input())
    arr = deque(map(int, input().split()))

    # print(arr)

    first_num = 1
    count = 1  # 뺄 숫자
    while True:  # first_num > 0:
        # 무한루프 - 왜냐하면 내부에 종료조건이 있기 때문에 / if문으로 append()하는게 달라지고 break시킬거니까
        if count > 5:
            # 5를 넘으면
            count = 1
        first_num = arr.popleft()
        first_num -= count  # 해당하는 숫자만큼 뺀다
        if first_num <= 0:
            # 만약 0보다 작으면
            arr.append(0)
            break  # 만약 여기서 break 안 넣을거면 while조건 바꾸기
        else:
            # 0보다 작지 않으면
            arr.append(first_num)
        count += 1
    print(f'#{test_number} {" ".join(map(str, arr))}')
