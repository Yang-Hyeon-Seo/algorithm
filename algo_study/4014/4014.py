import sys
# sys.stdin = open('input.txt')
sys.stdin = open('sample_input.txt')


def func(N, X, arr):
    count = 0
    for i in range(N):
        # print(i, '번째 줄')
        need_slope = 0  # 0이면 슬로프 필요 X, 1이면 필요함
        height = 0
        length = 0
        for j in range(N):
            # print(height, length)
            if height == arr[i][j]:
                # print('높이 같음', height, arr[i][j])
                length +=1
                if need_slope == 1 and length >= X:
                    # print('슬로프 설치')
                    need_slope = 0
                    length -= X

            elif height > arr[i][j]:  # 낮아진 경우
                # print('높이 낮아짐', height, arr[i][j])

                if height - arr[i][j] > 1:
                    # print('절벽임')
                    break  # 2칸 이상 절벽

                need_slope = 1
                # print(need_slope)
                # 앞을 보면서 확인하는거임
                height = arr[i][j]
                for next in range(X):
                    if j + next >= N or arr[i][j + next] != height:
                        need_slope = 2  # 슬로프 설치 불가능이라는 의미로 그냥 변수 재사용함
                if need_slope == 2:
                    # print('앞에 설치 불가능')
                    break

                length = 1

            elif height < arr[i][j]:  # 높아진 경우
                # print('높이 높아짐', height, arr[i][j])

                if arr[i][j] - height > 1 and j != 0:
                    # print('절벽')
                    break

                if j != 0 and length < X:  # 활주로 건설 불가  # need_slope == 1 and
                    # print('길이 부족함')
                    break
                else:
                    # print('설치')
                    height = arr[i][j]
                    length = 1
            if j + 1 == N and need_slope == 1:  # 마지막인데 슬로프가 필요한 경우
                # print('마지막인데 길이 부족함')
                break
        else:  # break 안 만나고 나오면
            # print('활주로 ok')
            count += 1

    return count


T = int(input())
for test_case in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # print(N, X)
    # for i in range(N):
    #     print(arr[i])

    result += func(N, X, arr)

    # print(result, '돌림')
    result += func(N, X, list(map(list, zip(*arr[::-1]))))
    # result += func(N, X, list(map(list, zip(*arr))))

    # print(result)

    print(f'#{test_case} {result}')
