"""
스위치 켜고 끄기
1부터 연속적으로 번호가 붙어 있는 스위치들이 있음
스위치는 꺼져 있거나 켜져 있음
학생 몇 명을 뽑아서 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 나눠줌
학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치 조작

남학생 - 스위치의 번호가 자기가 받은 수의 배수이면 그 스위치의 상태를 바꿈
        - 스위치가 꺼져 있으면 켜고, 켜져 있으면 끔
여학생 - 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로
        좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서
        그 구간에 속한 스위치의 상태를 바꿈
        구간에 속한 스위치의 개수는 항상 홀수

입력
첫줄에는 스위치의 개수
스위치의 개수는 100이하인 양의 정수
두번쨰 줄에는 각 스위치의 상태가 주어짐
켜져 있으면 1, 꺼져 있으면 0
셋째 줄에는 학생 수가 주어짐
학생 수는 100 이하의 정수
넷쨰 줄부터 마지막줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어짐
남학생 : 1 / 여학생 : 2
학생이 받은 수 <= 스위치의 개수, 양의 정수

출력
스위치의 상태를 1번 스위치부터 마지막 스위치까지 한 줄에 20개씩 출력함
"""

# 입력
"""
8
0 1 0 1 0 0 0 1
2
1 3
2 3
"""
"""
45
0 0 0 0 0 0 1 1 1 0 1 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1
2
1 5
2 13
"""
# 출력
"""
1 0 0 0 1 1 0 1
"""
"""
0 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 0 1 
0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 
1 1 1 1 0 
"""


N = int(input())  # 스위치의 개수
arr = [0] + list(map(int, input().split()))  # 스위치의 상태 / 0이면 꺼짐 / 1이면 켜짐
# 0번쨰 인덱스는 사용X

Students = int(input())  # 학생의 수
for i in range(Students):
    # 학생 수 만큼 반복하면서 학생 성별, 스위치 번호를 받음
    gender, number = map(int, input().split())
    if gender == 1:   # 남학생이라면
        now_switch = number  # 현재 스위치 번호 받기
        while now_switch <= N:  # number의 배수마다 다 바꾸기
            arr[now_switch] = (arr[now_switch] + 1) % 2  # 0이면 1, 1이면 0이 됨
            now_switch += number  # number만큼 더하면 number의 배수가 됨 ㅎㅂㅎ
    else:  # 여학생이라면
        # 현재 위치 상태 바꾸기
        arr[number] = (arr[number] + 1) % 2
        # now_switch = number  # 현재 위치 (필요할지는 모르겠음)
        left_switch = number-1  # 왼쪽 스위치
        right_switch = number+1  # 오른쪽 스위치
        move = 0  # 몇 번 이동했는지 의미
        while left_switch > 0 and right_switch <= N and arr[left_switch] == arr[right_switch]:
            # 왼쪽 스위치가 0보다 크고(0 포함 X), 오른쪽 스위치가 N과 같거나 작고(N 포함 O), 둘의 값이 같다면
            arr[left_switch] = (arr[left_switch] + 1) % 2  # 0이면 1, 1이면 0이 됨
            arr[right_switch] = (arr[right_switch] + 1) % 2  # 0이면 1, 1이면 0이 됨
            left_switch -= 1
            right_switch += 1

for i in range(1, N+1):
    print(arr[i], end=' ')
    if i % 20 == 0:  # 20의 배수라면
        print() # 줄바꿈