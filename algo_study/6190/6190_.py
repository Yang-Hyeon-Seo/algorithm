"""
6190_정곤이의 단조 증가하는 수 _D3
자신이 엄청난 수학자임을 증명
어떤 규칙을 만족하는 수를 찾아보기로 함

단조 증가하는 수
각 숫자의 자리수가 단순하게 증가하는 수 의미

k자리수 X(d1 < d2 < d3< d4 ...)를 만족하면 단조 증가하는 수
= 높은 자리수가 낮은자리수보다 항상 작음

양의 정수 N개가 주어지는데
두 값을 곱한 값이
단조 증가하는 수인것들을 구하고
그중에 최댓값을 출력
"""

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    # number_list = []
    max_num = -1

    for i in range(N-1):
        for j in range(i+1, N):  # i < j
            multied = arr[i] * arr[j]
    # 일단 두 수를 곱한게 단조 증가하는 수라면 리스트에 추가
        # 1. 두 수를 곱한다
            multied_str = str(multied)
            # print(multied)
            for num in range(len(multied_str)-1):
                if multied_str[num] >= multied_str[num+1]:
                    break
            else:
                if max_num < multied:
                    max_num = multied
                # number_list.append(multied)
    # 2. 곱한 수를 문자로 바꾼 후에 돌면서 뒷자리 수가 더 크면 OK
    # 반복문 돌면서 만약 뒷자리 수가 더 작으면 break
    # for-else문 이용해서 break안하고 끝났다면 append
    # print(max_num)
# 리스트 안에 있는 것들 중 가장 큰 수를 출력
    print(f'#{test_case} {max_num}')