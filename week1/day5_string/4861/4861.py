"""
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라고 함
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램
회문은 1개가 존재하는데, 가로뿐만 아니라 세로로 찾아질 수도 있음
N과 M은 주어짐
"""
# 아이디어
"""
현재 위치에서부터 M 개 만큼 오른쪽에 있는 문자, 아래에 있는 문자를 받아서 회문 여부 확인
회문 여부 확인하는 함수 만들기
회문은 1개가 존재한다고 했기 때문에, 회문을 찾으면 return
"""

import sys


# 회문 여부를 확인하는 함수
def is_palindrome(str_list, M):
    """
    문자 리스트를 받아서 회문인지 확인
    :param str_list:
    :param M: 문자 리스트의 길이
    :return: 회문이면 1, 회문이 아니면 0
    """
    reversed_str = []
    for i in range(M-1, -1, -1):  # 뒤 인덱스부터 reversed_arr 추가
        reversed_str.append(str_list[i])

    if reversed_str == str_list:  # reversed_arr, arr 값이 같은지 확인
        return 1
    else:
        return 0


# 회문 찾는 함수
def find_palindrom(arr, N, M, dr, dc): # arr, arr 길이, M(회문 길이), dr, dc
    """
    회문 찾는 함수
    찾으면 회문을 반환, 못 찾으면 'None' 반환
    회문은 1개 존재
    """
    # arr 순회
    # M만큼 덜 가는 이유는 그러면 벽 체크를 안해도 되니까
    for r in range(N):
        for c in range(N):
            for check in range(2):
                # 문자 리스트 만들기
                message = []
                for m in range(M): # 자기자신도 포함해야 하니까 0부터 시작
                    nr = r + dr[check] * m
                    nc = c + dc[check] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        message.append(arr[nr][nc])
                # 회문 여부를 확인하는 함수 적용
                # 길이가 M이라면
                if len(message) == M:
                    result = is_palindrome(message, M)
                    #print(result)
                # 만약 회문이면 리턴
                    if result == 1:
                        return message


sys.stdin = open('sample_input.txt')

# 입력받기
T = int(input())

# 델타(오른쪽, 아래)
dr = [0, 1]
dc = [1, 0]

for test_case in range(1, T + 1):
    # print("test", test_case)
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]   # 문자가 들어 있는 2차원 리스트 형태

    palindrome = find_palindrom(arr, N, M, dr, dc)

    print(f'#{test_case} {"".join(palindrome)}')
