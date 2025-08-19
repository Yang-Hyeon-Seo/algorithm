import sys

# sys.stdin = open('Sample_input.txt')
sys.stdin = open('input.txt')


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 이 리스트 안에 있는 내용을 인덱스로 사용하기
    check = [1] + [0] * (N-1)  # 방문 여부 체크, 첫번째 방은 항상 오른쪽으로 감
    count = 0  # 포탈 이용 횟수 카운트
    print(arr)
    print(check)

    # idx = 0

    idx = 1
    count = 1
    print(idx)
    print(count)
    while idx < N-1:  # N-1에 도착하는 순간 종료
        if check[idx] < 1:
            check[idx] += 1
            idx = arr[idx] - 1
            count += 1
            print('왼쪽 이동', count, idx)
        else:  # 1보다 큰 경우 오른쪽으로 이동
            count += 1
            idx += 1
            print('오른쪽 이동', count, idx)


    print(f'#{test_case} {count}')


