"""
쇠막대기 절단
쇠막대기를 아래에서 위로 겹쳐놓고, 레이저를 위에서 수직으로 발사하여 절단
배치 조건
- 쇠막대기는 자신보다 긴 막대기 위에만 놓일 수 있음
- 쇠막대기를 다른 쇠막대기 위에 놓는 경우, 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 함
- 각 쇠막대기를 자르는 레이저는 적어도 1개 존재
- 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음
쇠막대기와 레이저의 배치가 주어졌을 때, 잘려진 조각의 총 개수 구하기
"""

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    arr = input()
    previous = ''  # 직전 값 저장하기
    count = 0  # '('의 수 계산
    pieces = 0  # 조각의 수

    # 입력받은 문자열 순회
    for i in arr:
        if i == '(':
            count += 1
            previous = '('

        # 들어온 값이 )
        # previous == '('인 경우 -> 레이저
        elif previous != ')':
            count -= 1
            pieces += count
            previous = ')'
        # previous == ')'인 경우 -> 쇠막대 종료
        else:
            count -= 1
            pieces += 1
            previous = ')'
    print(f'#{test_case} {pieces}')