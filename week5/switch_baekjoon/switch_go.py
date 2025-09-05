''' 시나리오
1 = 스위치 켜짐, 2 = 스위치 꺼짐
case1. 남학생의 경우 : 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꿈
case2. 여학생의 경우 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭이며 가장 많이 포함하는 구간을 찾아서
                     그 구간에 속한 스위치를 모두 바꿈
남학생의 경우 스위치번호 % 3 == 0 이면 스위치를 바꾸는데 스위치 바꾸는걸 코드로 어떻게 구현???
여학생의 경우 좌우 대칭으로 가장 많이 포함하는 구간을 먼저 찾고 스위치를 바꿔야함 > 대칭인 가장 긴 구간을 찾아야 하기때문에
이부분 while문 접근, 스위치 바꾸는 과정은 남학생 경우처럼 구현 >> 이부분을 코드로 어떻게 적어야하지??
'''


N = int(input())    # 스위치 갯수
switch = list(map(int, input().split()))    # 스위치 상태
# print(switch)
students = int(input())

for _ in range(students):  #  학생 수 만큼 순회
    gender, num = map(int, input().split())     # 성별과, 학생이 받은 수

    if gender == 1:  # 성별이 남자이면
        for i in range(num-1, N, num):  # 0-base 이므로 num-1 부터 시작
            switch[i] = (switch[i] + 1) % 2  # 스위치가 1이면 0으로 바꾸고 스위치가 0이면 1로 바꿈

    elif gender == 2:   # 성별이 여자인경우 >> 어떻게 구현해야할지 몰라서 찾아본 부분
        left = num - 1  # 왼쪽과 오른쪽값을 똑같이 중앙 기준값으로 리셋
        right = num - 1

        # while문으로 구현해야 겠다고는 생각했는데, left 와 right 를 초기값 num 으로 설정해서 양옆으로 뻗어나가는 논리를 생각 못함.
        # 벽체크와 초기값 중심으로 -1, +1 함으로써 대칭이면
        while left - 1 >= 0 and right + 1 < N and switch[left-1] == switch[right+1]:
            left -= 1   # 왼쪽으로 한칸씩 확장
            right += 1  # 오른쪽으로 한칸씩 확장

        for i in range(left, right+1):  # while 문 밖으로 빼서 한번에 토글
            switch[i] = (switch[i] + 1) % 2


for i in range(1, N + 1):
    print(switch[i - 1], end=' ')   # 0base라 switch[i-1]로 출력, end = ' ' 를 통해 출력마다 공백으로 연결
    if i % 20 == 0: # i가 20의 배수일 때마다
        print() # 줄바꿈 넣기
