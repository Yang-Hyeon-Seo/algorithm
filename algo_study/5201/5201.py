"""
5201_컨테이너 운반
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 함
트럭 당 한개의 컨테이너를 운반할 수 있고, 트럭의 적재 용량을 초과하는 컨테이너는 운반할 수 없음

이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮김
옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램
화물을 싣지 못한 트럭이 있을 수 있음
남는 화물이 있을 수 있음
컨테이너를 한개도 옴ㄹ기지 못하면 0 출력

"""

import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N : 컨테이너 수 / M : 트럭 수
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)
    # print(container, truck)

    count = 0  # 옮긴 수


    truck_number = 0  # 트럭 인덱스
    container_number = 0  # 컨테이너 인덱스
    while truck_number < M and container_number < N:
        # print(truck[truck_number], container[container_number])
        if truck[truck_number] >= container[container_number]:
            # 옮길 수 있음
            count += container[container_number]  # 컨테이너 용량만큼 더하기
            truck_number += 1  # 다음 인덱스 확인
            container_number += 1

        else:
            # 옮길 수 없음(트럭의 용량이 더 작음(
            container_number += 1  # 다음 컨테이너로 옮김

    print(f'#{test_case} {count}')

