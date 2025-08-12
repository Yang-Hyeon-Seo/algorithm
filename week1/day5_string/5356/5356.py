"""
5개의 문자열을 받고
이를 세로로 읽는데
글자가 없으면 그냥 다음줄로 넘어감
[0][0]부터 [9][9]까지 공백없이 글자 출력
"""

import sys

sys.stdin = open("sample_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    # 5개의 문자열 입력받기
    strings = [input() for _ in range(5)]

    result = []

    # 앞에서부터 하나씩 읽어가기
    # 가장 긴 문자열이 뭔지 모르니까, max_length 계산할까?
    max_length = 0
    for i in range(5):
        now_length = len(strings[i])
        if max_length < now_length:
            max_length = now_length

    # 가장 긴 문자열 길이만큼 반복
    for c in range(max_length):
        for r in range(5):  # 5줄
            if c >= len(strings[r]):
                continue
            result.append(strings[r][c])
    print(f'#{test_case} {"".join(result)}')