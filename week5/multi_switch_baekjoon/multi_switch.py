"""
배수 수위치
강호는 전구 N개를 가지고 있음
전구는 1번부터 N번까지 번호가 매겨져 있고, 일렬로 놓여져 있음
전구는 켜져 있거나 꺼져 있음

강호는 모든 전구를 끄려고 함
전구를 켜고 끌 수 있는 스위치 N개를 가지고 있음
스위치도 1~N번 번호가 매겨져 있음
i번 스위치는 i의 배수 번호를 가지고 있는 전구의 상태를 모두 반전함

모든 전구를 끄기 위해서 스위치를 몇 번 눌러야 할까?

"""

#
# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for test_case in range(1, T+1):  # 제출할 땐 이 부분 지우고, 인덴트도 하나 줄여야 함

arr = [0] + list(input())  # 첫번째 인덱스는 사용 안함
N = len(arr)
# print(arr)
# 아이디어 1 : 앞에서부터 하나씩 하면 되지 않음?
count = 0  # 지금까지 누른 횟수
for i in range(1, N):
    if arr[i] == 'Y':
        count += 1
        j = i
        while j < N:
            if arr[j] == 'Y':
                arr[j] = 'N'
            else:
                arr[j] = 'Y'
            j += i
        # print(arr)
print(count)
