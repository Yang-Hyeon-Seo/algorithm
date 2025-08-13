"""
4864_문자열비교
두개의 문자열 str1, str2가 주어짐
문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램 만들기
첫 문자열이 두번째 문자열 안에 존재하면 1, 존재하지 않으면 0 출력

brute_force 기법 사용하기
"""

# brute_force
"""
문자열1 돌면서
문자열2와 동일한지 하나씩 확인하면서
틀리면 1칸씩 이동하는 방법
"""

# 아이디어
"""
brute_force 함수 만들어서 진행하기(함수 만드는 연습)
함수를 기능별로 만들어서 
"""

import sys

sys.stdin = open('sample_input.txt')


# brute_force 함수
def brute_force(str1, str2):
    # for i in range(len(str2)):  # str2 순회하면서
    for i in range(len(str2) - len(str1) + 1):  # str1을 비교할 공간이 남아있는 곳까지만 순회하도록 수정
        for j in range(len(str1)):  # str1 안의 값이 str2에 있는지 확인하기
            # if i + j >= len(str2):  # 범위를 초과했을 수도 있음
            #     break
            if str2[i + j] != str1[j]:  # str1의 현재 값이 str2의 현재 값과 동일하지 않다면
                break
            # 동일하다면 그냥 다음 문자로 넘어가면 됨
            # 만약 j가 len(str1) - 1까지 왔다면 -> 끝까지 동일하다는 의미
            if j == len(str1) - 1:
                return 1
    # 문자열이 동일하지 않음
    return 0


# 수업 과정에서 배운 방법
def brute_force_while(str1, str2):  # str1 패턴, str2 문자열
    j = 0  # str1 인덱스
    i = 0  # str2 인덱스
    M = len(str1)  # str1 길이
    N = len(str2)  # str2 길이
    while j < M and i < N:  # str1, str2의 길이보다 짧은 경우동안 진행됨
        if str2[i] != str1[j]:  # 두 값이 다르다면
            i = i - j  # j만큼 돌아감
            j = -1
        i += 1
        j += 1
    if j == M: return 1  # 성공
    else: return 0  # 실패



# 입력받기
T = int(input())
for test_case in range(1, T + 1):
    str1 = input()  # 첫 번째 문자열
    str2 = input()  # 두 번째 문자열

    # brute_force 함수
    result = brute_force_while(str1, str2)

    # 출력
    print(f'#{test_case} {result}')

"원래 brute_force 함수(강의)"


