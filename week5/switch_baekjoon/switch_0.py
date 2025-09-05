# 함수 정의
def last_switch(switch_count, switch, student_info):
    """
    학생들이 스위치의 상태를 바꾸었을 때,
    스위치의 마지막 상태를 출력하는 함수

    :param switch_count: 스위치의 개수
    :param switch: 스위치의 초기 상태
    :param student_info: 학생의 성별과 학생이 받은 수를 담은 리스트
    """

    for gender, number in student_info:                     # 리스트로부터 순서대로 학생의 정보 불러오기
        if gender == 1:                                     # 남학생일 경우
           for i in range(switch_count):
                if (i + 1) % number == 0:                   # 스위치 번호(i + 1)가 자기가 받은 수의 배수이면
                    change_on_off(switch, i)                # 그 스위치의 상태를 바꾼다

                else:                                       # 그렇지 않을 경우 넘어간다
                    continue

        else:                                               # 여학생일 경우 (gender != 1)
            change_on_off(switch, number - 1)               # 자기가 받은 수의 스위치만 상태는 항상 바꿈

            left = number - 2                               # 인덱스 (number - 1) - 1 = number - 2
            right = number                                  # 인덱스 (number - 1) + 1 = number

            # 좌우 대칭 위치에 놓인 스위치의 상태가 동일하다면
            while switch[left] == switch[right] and 0 <= left and right < switch_count:
                change_on_off(switch, left)
                change_on_off(switch, right)                # 두 스위치의 상태를 바꾼다

                left -= 1
                right += 1                                  # 탐색을 위해 양방향 각각 이동

    return switch


def change_on_off(switch, idx):
    """
    스위치의 상태를 반대로 바꾸는 함수

    :param switch: 스위치의 상태
    :param idx: 스위치의 번호
    """

    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0


# 스위치의 개수 N
N = int(input())

# 각 스위치의 상태
switch_status = list(map(int, input().split()))

# 학생의 수 M
M = int(input())

# 학생의 성별과 학생이 받은 수를 담을 리스트 생성, 튜플로 저장
student_information = []

for _ in range(M):
    student_gender, student_number = map(int, input().split())
    student_information.append((student_gender, student_number))

result = last_switch(N, switch_status, student_information)
for i in range(0, len(switch_status), 5):
    print(result[i:i+5])