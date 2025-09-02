"""
5431_민석이의 과제 체크하기
민석이는 교수가 되었고, 이번에 처음으로 맡은 과목에 수강생이 N명임
1버누터 N번까지의 번호가 매겨져 있고
어떤 번호의 사람이 제출했는지에 대한 목록을 받음
과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램
"""

import sys
sys.stdin = open('sample_input.txt')

T= int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    submit_arr= list(map(int, input().split()))
    arr = [i for i in range(1, N+1) if i not in submit_arr]
    print(f'#{test_case} {" ".join(map(str, arr))}')
