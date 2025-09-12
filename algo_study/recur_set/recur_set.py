"""
연습문제2_부분집합
재귀, 가지치기 이용
"""

# # 입력
# arr = list(range(1, 11))
#
# # powerset 중 원소의 합이 10인 부분집합 구하기
#
# # 비트연산 이용하기
# N = len(arr)
# # count = 0
# for i in range(1<<N):  # 2ⁿ번 반복
#     for j in range(N):  # N번 반복
#         if i & (1 << j):
#             print(arr[j], end=" ")
#     # count += 1
#     print()
# # print(count)