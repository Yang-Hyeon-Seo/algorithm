# '''
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 구하시오
# '''

# 입력 가지고 오기
import sys
sys.stdin = open('sample_input.txt')

# 입력 받기
T = int(input()) # 테스트 케이스만큼 반복
#print(T)
for test_case in range(1, T+1):
    N = int(input()) # 배열의 길이
    arr = list(map(int, input().split()))
    #print(arr)

    # bubble sort
    # 리스트의 0번 인덱스부터 시작
    # 0번 인덱스와 1번 인덱스 비교
    # 만약 0번 인덱스가 1번 인덱스보다 크다면 자리 교환 / 아니면 그냥 지나가기
    # 그 이후에 인덱스 각각 1씩 증가
    for i in range(N-1, 0, -1): # 1번 인덱스부터 N번 인덱스까지 반복 / 점점 숫자 작아짐(뒤에서부터 채워지니까)
        for j in range(0, i): # 0번 인덱스부터 i-1번 인덱스까지 반복 / 점점 최고 숫자 작아짐(뒤는 채워지니까)
            if arr[j] > arr[j+1]: #오른쪽 값이 더 작다면 교환 (내림차순이라면 오른쪽 값이 클 때 교환)
                arr[j], arr[j+1] = arr[j+1], arr[j]
    result = arr[-1] - arr[0]
    print(f'#{test_case} {result}')




