"""
0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때,
3장의 카드가 연속적인 번호를 갖는 경우를 run이라고 하고
3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 함
그리고 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin이라고 부름
6자리 숫자를 입력 받아 baby-gin 여부를 판단하기
"""

import sys
sys.stdin = open('input.txt')

# 똑같은 것 먼저 찾아 없애고
# 연속되는 것 없애기

T = int(input())
for test_case in range(1, T+1):
    arr = list(input())
    N = len(arr)
    numbers = [0] * 10  # 0~9 사이의 임의의 카드들
    for i in arr:
        numbers[int(i)] += 1
    print(numbers)

    count = 0

    for i in range(10):
        if numbers[i] == 3:
            numbers[i] -= 3
            count += 1
    while count < 2 and # 2보다 작다 == babygin이 아니다 and
    if count == 2:
        print(True)
    else: