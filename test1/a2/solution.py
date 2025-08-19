import sys

sys.stdin = open('Sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    min_score = float('inf')

    # 만들 수 있는 최대 보너스 묶음의 수
    max_bonus_groups = M // K

    # c: 초반에 연속으로 만들 보너스 묶음의 개수 (0개 ~ 최대 개수)
    for c in range(max_bonus_groups + 1):
        # 1. c개의 보너스 묶음을 만들고 남은 맞힌 문제의 수
        remaining_m = M - c * K
        # 사용할 수 있는 틀린 문제(칸막이)의 수
        num_incorrect = N - M

        # 2. 남은 문제들을 보너스 없이 배치할 수 있는지 확인
        separators_needed = 0
        if remaining_m > 0:
            # 남은 문제들을 K-1개 이하의 묶음으로 나누려면 몇 개의 칸막이가 필요한지 계산
            # (A // B)는 내림이지만, (A + B - 1) // B는 올림과 같은 효과
            num_safe_groups = (remaining_m + (K - 1) - 1) // (K - 1)
            separators_needed = num_safe_groups - 1

        # 가진 칸막이(틀린 문제)로 남은 문제들을 나눌 수 있다면 유효한 전략
        if num_incorrect >= separators_needed:
            # 3. 유효하다면, 점수 계산
            score = 0
            # c번의 보너스를 받았을 때의 점수 계산
            for _ in range(c):
                # K개의 문제(각 1점)를 풀고 점수가 2배가 됨
                score = (score + K) * 2

            # 남은 문제들은 각각 1점씩만 더함
            total_score = score + remaining_m

            # 4. 최솟값 갱신
            min_score = min(min_score, total_score)

    print(f'#{tc} {min_score}')
