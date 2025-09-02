"""
3499_퍼펙트 셔플_D3

"""

# 인덱스/슬라이싱 이용해서 하나씩 넣고 그러면 되는 거 아님?

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 카드의 수
    arr = list(input().split())  # 입력받은 카드

    """
    홀수인 경우에 앞쪽 카드 덱에 한 장 더 들어가게 됨(test_case 3번)
    이 경우 0 1 2 인덱스가 앞 덱, 3 4가 뒤 덱에 들어가니까
    일단 덱이 홀수/짝수에 따라서 덱의 인덱스를 나눠서 덱을 만들고
    """
    shuffle = N//2  # N의 절반값 / 첫번째 덱 기준으로 반복할 횟수 의미

    if N%2 == 0:
        deck1 = arr[: shuffle]  # 첫번째부터 N//2-1까지
        deck2 = arr[shuffle:]    # N//2번 인데스부터 마지막까지
        shuffle = N//2  #
    else:
        # 여기에서는 N//2+1번까지 들어가야 함
        shuffle += 1  # N//2 + 1 의미 (더하는 이유 : 첫번째 덱은 N//2보다 1이 더 많기 때문)
        deck1 = arr[:shuffle]  # 첫 번째부터 N//2까지 - 3번 테스트케이스 기준 0, 1, 2
        deck2 = arr[shuffle:]  # N//2+1부터 마지막까지

    # print(deck1)
    # print(deck2)

    result = []  # 결과 담을 리스트
    for i in range(shuffle):  # shuffle 만큼 반복하면서 result에 append하고, 만약 deck2의 길이가 i보다 작으면 그냥 break
         result.append(deck1[i])
         if i < len(deck2):  # 먄악 i가 deck2의 길이보다 크다면(덱이 홀수고, 현재 인덱스는 deck2에 없는 경우에)
             result.append(deck2[i])
             # 원래는 i >= len(deck2): break 이렇게 하려고 했는데, 어차피 계속 조건을 확인하니까  안에 넣는게 더 좋을것 같다고 생각함

    print(f'#{test_case} {" ".join(result)}')