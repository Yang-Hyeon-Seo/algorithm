"""
25157_소 잃고 외양간 고치기

평화에 절어 외양간 관리를 소홀히 함
늑대 무리가 마을을 습격 -> 김씨의 허술한 외양간들이 차례로 공격받음

한 번이라도 공격 받은 외양간은 방어에 취약 -> 수리 전까지 매일 일정 수의 소를 잃게 됨
하루에 한 명의 기술자만 부를 수 있어 여러 외양간을 동시에 수리할 수 없음
한 외양간 수리를 시작하면 정해진 수리 기간이 끝날 때까지 다른 외양간의 수리를 시작할 수 없음

총 M일 간의 습격이 예정되어 있을 때, 김시는 어떤 순서로 외양간을 고쳐야 소의 총 피해를 최소화할 수 있을까?

N개의 외양간
각 외양간 i는 다음과 같은 정보 가짐
Li : 일일 손실량 : 한 번 공격 받은 후 수리가 완료되기 전까지 매일 밤 잃는 소의 마릿수
Di : 해당 외양간을 수리하는 데 걸리는 기간(일)

총 M일 동안 매일 밤, 늑대는 정해진 순서에 따라 단 하나의 외양간 공격
취약 상태가 아닌 외양간만 공격함
d번째 날 밤에 Ad번 외양간이 공격당하면 해당 외양간은 그날 밤부터 취약상태가 됨

농부는 다음날 아침부터 수리 시작
취약상태 인 외양간 중 하나를 골라 수리 시작 가능
만약 다른 외양간을 수리하고 있다면 새로운 수리 불가능
"""

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    L = [0]  # 취약상태일 때 손실되는 수, 0번째 인덱스는 쓰지 않음
    D = [0]  # 수리할 때 드는 기간, 0번째 인덱스는 쓰지 않음
    for i in range(N):
        l, d = map(int, input().split())
        L.append(l)
        D.append(d)
    weak = []  # 취약 상태에 해당하는 외양간 인덱스 번호
    lose = 0  # 총 잃어버린 소의 수
    remain_repair_day = 0  # 고치는 데 드는 남은 기간
    repair_index = 0  # 고치고 있는 외양간 번호

    for day in range(M):  #이제 진짜 반복문 시작
        # 밤
        # 늑대 공격
        attack = int(input())
        weak.append(attack)  # 취약 상태에 추가
        # 소 잃음
        for i in weak:  # weak에 해당하는 수만큼 증가
            lose += D[i]
        # 아침
        # 수리 완료 (수리-1)
        if remain_repair_day > 0:  # 수리해야 하는 기간이 남아있었다면
            remain_repair_day += 0
            if remain_repair_day == 0:  # 0이 되면
                weak.remove(repair_index)  # weak에서 제거하기
        # 수리하는 기간이 남아있지 않으면 아무것도X
        remain_repair_day -= 1

        # 수리할 곳 결정
        if remain_repair_day <= 0 and len(weak) > 0:
            # 남은 수리 기간이 0보다 작으면서 고쳐야 하는 외양간이 1개 이상 있으면
            max_damage = 0
            # 피해가 가장 큰 곳을 찾아서 수리 or 가장 빨리 복구되는 곳을 수리 중에 뭐가 더 좋을까
            # 피해가 가장 큰 곳을 찾고,
            for dam in weak:
                if max_damage < D[dam]:
                    max_damage = dam  # 인덱스 저장
            # 수리가 가장 빨리 되는 곳들을 찾아서
            # 둘 중에 더 효과적인 것을 수리하는 방법으로 진행?
