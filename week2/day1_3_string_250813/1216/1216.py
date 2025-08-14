"""
1216_회문2
회문 : palindrome
100x100 평면에서 가로, 세로 모두 보아 가장 긴 회문의 길이 구하기
글자는 A, B, C중 하나
글자판은 무조건 정사각형
ABA도 회문, ABBA도 회문, A도 회문임
각 회문에 대해 직선으로만 판단

10개의 테스트 케이스
테스트 케이스 번호가 입력됨
"""

import sys
sys.stdin = open('input.txt')


# 회문 여부 확인하는 함수
def is_palindrome(string, length):
    """
    회문 여부 확인하는 함수
    :param string: 확인할 문자열
    :param length: 문자열 길이
    :return: 회문 길이 또는 0 반환
    """
    for i in range(length//2):
        if string[i] != string[length-1-i]:
            # 회문 아님
            return 0  # 0 반환
    return length  # 회문 길이 반환


# arr 탐색하는 함수
def find_max_palindrome(arr, N):
    max_length = 1  # 회문 최대 길이 저장, 문자 1개만 있는 것도 회문이니까 일단 최소값은 1
    for i in range(N):
        for j in range(N):
            # arr 돌면서
            for k in range(j+1, N):
                if arr[i][j] == arr[i][k]:  # 두 문자가 같은 순간이 오면
                    length = k - j + 1  # 문자열 길이
                    if is_palindrome(arr[i][j:k+1], length) > max_length:
                        max_length = length
                    #print(length, max_length, arr[i][j:k+1])
    return max_length


T = 10
for test_case in range(1, T + 1):
    tc = input().strip()
    N = 100  # 100x100 평면이기 때문
    arr = [input() for _ in range(N)]

    '''
    회문을 어떻게 찾지?
    현재 문자랑 같은 문자가 나오면 길이 재서 회문 여부 확인(끝까지 가기)
    회문이면 현재 길이 저장 / max보다 길면 max갱신
    현재 위치에서 없으면 다음 칸으로 이동하기
    '''
    max_length = -1  # 갱신 된건지 확인하기 위해 -1 넣음

    for array in [arr, list(map(list, zip(*arr[::-1])))]:
        length = find_max_palindrome(array, N)
        if max_length < length:
            max_length = length



    print(f'#{tc} {max_length}')