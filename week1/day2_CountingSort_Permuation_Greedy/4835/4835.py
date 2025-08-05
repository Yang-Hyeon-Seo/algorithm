'''
길이가 N인 리스트 안에서
연속한 M개의 합이 가장 큰 것과 작은 것 구해서
차이 출력
'''

# input 받기
import sys
sys.stdin = open('sample_input.txt')

# testcase
T = int(input())
for test_case in range(1, T+1):
    # N과 M 받기
    N, M = map(int, input().split())
    # 리스트 입력 받기
    arr = list(map(int, input().split()))
    # print(T, N, M, arr)

    # counting sort 이용하는 방법 생각해보기


    # counting sort 이용하지 않는 방법
    # 길이가 N인 리스트 안에서 연속한 M개의 합 구하기
    # 반복은 M개씩 뭉쳐서 다니니까 N보다 적어짐
    min_num = 999999999999999999 # 엄청 큰 수
    max_num = -99999999999999999 # 엄청 작은 수
    for i in range(N-M+1): # 0부터 N
        # 만약 0~5, 3개씩이라고 하면
        # 012, 123, 234, 345
        # len은 6인데 6-m을 하면 3이니까
        # range에 넣으려면 1을 더해야함
        sum = 0
        for j in range(M):
            sum += arr[i + j]

        if sum > max_num:
            max_num = sum
        if sum < min_num:
            min_num = sum

    # 큰 값과 작은 값 차이
    result = max_num - min_num
    print(f'#{test_case} {result}')