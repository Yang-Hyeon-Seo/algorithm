'''
가로 길이는 100
상자의 높이는 1이상 100이하
덤프 횟수는 1이상 1000이하
제일 높은 부분과 제일 낮은 부분의 차이 구하기
'''

# 입력 받아 오기
import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 수가 안 나와 있음 -> while문? 이용해서 돌리기
test_case = 1

def max_number(arr):
    '''
    arr에서 가장 큰 숫자 리턴
    '''
    max_num = 0
    for i in arr:
        if i > max_num: # i가 max_num보다 크면 max_num 갱신
            max_num = i
    return max_num

def counting_sort(arr):
    # arr 길이만큼 counts와 sorted_arr 만들기
    sorted_arr = [0] * len(arr)
    counts = [0] * (max_number(arr)+1)

    #counts 세기
    for i in arr:
        counts[i] += 1

    #counts 누적으로
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    # sorted_arr 만들기
    for i in range(len(arr)-1, -1, -1): # 뒤에서부터 하나씩
        # counts[arr[i]]가 가리키는 곳 -1이 arr[i]의 위치 / counts[arr[i]]도 -1이 진행되어야 함
        counts[arr[i]] -= 1
        sorted_arr[counts[arr[i]]] = arr[i]
    return sorted_arr



while test_case <= 10: # 총 10개의 테스트 케이스가 주어짐
    dump = int(input())
    hight_arr = counting_sort(list(map(int, input().split()))) # 정렬된 리스트로 입력
    # 정렬 수행
    # hight_arr = counting_sort(hight_arr)

    # dump의 횟수만큼 반복
    for i in range(dump):
    # 제일 뒤의 값에서 제일 앞으로 이동
        hight_arr[0] += 1
        hight_arr[-1] -= 1
    # 정렬 수행
        hight_arr = counting_sort(hight_arr)

        result = hight_arr[-1] - hight_arr[0]
    # 다시 정렬
        # 만약 평탄화가 완료되면
        if result <= 1: # 평탄화 완료 : 최고점 - 최저점 <= 1
            break

    # 출력
    print(f'#{test_case} {result}')

    test_case += 1

    # dump의 횟수만큼 반복
    # 정렬 수행
    # 제일 뒤의 값에서 제일 앞으로 이동
    # 다시 정렬



