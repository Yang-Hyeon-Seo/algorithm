# import sys
# sys.stdin = open('algo1_sample_in.txt')

"""
숫자 뒤에 숨겨진 패턴 찾기
길이 N 숫자열 -> 단순 증가 패턴
단순 증가 패턴 : 패턴내 숫자들이 감소나 정체 없이 꾸준히 증가(이전것보다 다음것이 크기만 하면 됨)
수열을 M인 윈도우로 나누어 윈도우 내에서 패턴을 찾기로 함
단순 증가 패턴을 가지는 윈도우는 몇개?

N이 M의 배수가 아닌 경우 마지막 윈도우는 남은 원소에 대해서만 증가패턴 확인함
윈도우 내의 숫자가 1개인 경우 단순증가패턴으로 간주함
"""


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N : 전체 숫자열 M : 윈도우의 크기
    arr = list(map(int, input().split()))
    idx = 0  # 반복하면서 확인 시작할 인덱스
    m_idx = 1  # M 안에서 반복하면서 확인할 인덱스 / 제일 처음은 1부터 시작
    count = 0  # 단순증가패턴 수
    pattern = True  # 단순증가패턴 여부 / 일단 True로 시작
    # last_number = arr[0]
    # now_number = arr[1]
    # print(arr)

    for i in range(N//M):
        # print('다음패턴')
        pattern = True
        last_num = arr.pop(0)
        for j in range(M-1):
            now_num = arr.pop(0)
            # print(last_num, now_num)
            if last_num >= now_num:
                # print('패턴 깨짐')
                # 패턴이 깨진 경우
                pattern = False

            if pattern and j == M-2:  # 패턴이라면
                # print('패턴임')
                count += 1
            last_num = now_num


    if len(arr) == 1:
        # print('마지막에 한 개 남음')
        count += 1
    elif len(arr) > 1:
        # print('마지막에 조금 남음(M개 이하)', len(arr))
        last_num = arr.pop(0)
        for j in range(len(arr)):
            now_num = arr.pop(0)
            if pattern:  # 패턴이라면
                if last_num >= now_num:
                    # 패턴이 깨진 경우
                    pattern = False
                if j == M-2:
                    count += 1

    # if N//M * M < N:


    print(f'#{test_case} {count}')


