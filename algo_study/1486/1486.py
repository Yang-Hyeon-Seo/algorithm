"""
1486_잔훈이의 높은 선반
높이가 B인 선반이 하나 있음
N명의 점원들이 장훈이가 선반 위에 올려 놓은 물건을 사용해야 하는 일이 생김
각 점원의 키는 Hi로 나타냄 - 점원들은 탑을 쌓아서 선반 위의 물건을 사용하기로 함

탑은 1명 이상으로 이루어짐
탑의 높이는 점원이 1명일 경우 그 점원의 키와 같음
2명 이상인 경우 탑을 만든 모든 점원의 키의 합과 같음

탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있음

높이가 B이상인 탑 중에 높이가 가장 낮은 탑을 알아낼 것
선반과 탑의 높이 차이 출력


"""
from itertools import combinations

import sys
sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    # N : 점원의 수, B : 선반의 높이
    arr = list(map(int, input().split()))
    tower = []

    for i in range(N+1):
        com = list(combinations(arr, i))
        for j in range(len(com)):
            height = sum(com[j])
            if height not in tower:
                tower.append(sum(com[j]))
        #print(tower)
    tower.sort()
    # print(tower)
    for i in range(len(tower)):
        if tower[i] >= B:
            print(f'#{test_case} {tower[i]-B}')
            break

    # # 완전탐색
    # # 부분집합
    # # 비트연산
    # # 모든 경우의 수는 2ⁿ (n : 점원의 수)
    # for i in range(1<<N):
    #     height = 0
    #     for idx in range(N):
    #         if i & (1 << idx):
    #             height += arr[idx]
    #     tower.append(height)
    #     # print(tower)
    #     pass
    # tower.sort()
    # result = 0
    # for i in range(len(tower)):
    #     if tower[i] >= B:
    #         # 처음 초과하게 되면
    #         result = tower[i] - B
    #         break
    #
    # print(f'#{test_case} {result}')