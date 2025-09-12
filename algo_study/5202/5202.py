"""
5202_화물도크
24시간 운영되는 물류 센터
화물을 싣고 내리는 도크가 설치되어 있음
0시부터 다음날 0시까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면
최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램
신청서에는 작업시작시간과 완료시간이 매시 정각을 기준으로 표시되어 있음
앞 작업 종료와 동시에 다음 작업 시작 가능

"""

import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    use_time = [tuple(map(int, input().split())) for _ in range(N)]
    print(use_time)
    use_time.sort()  # 앞의 숫자 기준으로 정렬됨
    print(use_time)
    time_inter = [use_time[i][1]-use_time[i][0] for i in range(N)]
    print(time_inter)
    use_time_inter = [(time_inter[i], use_time[i][0], use_time[i][1]) for i in range(N)]
    use_time_inter.sort()  # 앞의 숫자 기준으로 정렬
    print(use_time_inter)

    time_list = [0] * 24  # 0부터 23까지 0으로 채워진 리스트 - 시간 의미
    for i in range(N):  # N번 반복하면서
        if not time_list[use_time_inter[i][1]]# 0이면

            # 0이 아닌거 가지고 있으면 그냥 스루하기