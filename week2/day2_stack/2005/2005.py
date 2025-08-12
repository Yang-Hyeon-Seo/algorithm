"""
파스칼의 삼각형 출력
첫 번째 줄은 항상 1
두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자 합으로 구성됨

첫번째 값은 항상 1이지만, 대각선으로 보면, 1부터
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    stack = []  # 빈리스트 생성

    print(f'#{test_case}')

    for i in range(N):
        stack.append(1)
        tmp2 = stack[0]



        for j in range(1, i):
            tmp1, tmp2 = tmp2, stack[j]
            #print(tmp1, tmp2)
            stack[j] = tmp1 + tmp2
            #print(stack)
        # for j in range(i):
        #     stack.append(1)
            # for _ in range(1, j-1)

        print(' '.join(map(str, stack)))
