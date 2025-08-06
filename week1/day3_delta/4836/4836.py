'''
10x10 격자에 빨간색과 파란색을 칠하려고 함
칠이 끝난 후 색이 겹쳐 보라색이 된 칸의 수 구하기
'''

# 아이디어 1
'''
빨간색 + 1, 파란색 +1
결과가 2인 칸이 답이 될 것 같음!
'''
# 아이디어 2
'''
빨간색 1, 파란색2,
1 칠할 때 2가 있으면 3으로, 2 칠할 때 1이 있으면 3으로 해서
최종적으로 3인 칸이 답인 것으로
'''
# 아이디어 2번 채택
# 아이디어 3번
'''
빨간색, 파란색을 칠하려고 하는 좌표와 색깔을 리스트로 만들 것[[(r, c), color], [r, c, color], ... ]
새로 칠하면 append
만약 해당 좌표가 이미 존재하고, color가 다르다면 color 3으로 수정, result += 1
'''

# 아이디어 3번
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rectangle_list = [list(map(int, input().split())) for _ in range(N)]
    # 구성 : [start_r, start_c, end_r, end_c, color]
    # print(rectangle_list)


    color_list = []
    result = 0
    for i in range(N):
        # 그릴 사각형 정보 받아 오기
        start_r = rectangle_list[i][0]
        start_c = rectangle_list[i][1]
        end_r = rectangle_list[i][2]
        end_c = rectangle_list[i][3]
        color = rectangle_list[i][4]
        for r in range(start_r, end_r + 1):
            for c in range(start_c, end_c + 1):
                # 만약 해당 튜플이 이미 있다면
                for p in range(len(color_list)):
                    if (r, c) in color_list[p]:
                        # 색깔을 3으로 바꾸기
                        color_list[p][-1] = 3
                        result += 1
                color_list.append([(r, c), color])
        #print(color_list)
    print(f'#{test_case} {result}')




# 아이디어 2번
# 입력 받기
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 사각형을 몇 개 그릴 건지
    rectangle_list = [list(map(int, input().split())) for _ in range(N)]
    # 구성 : [start_r, start_c, end_r, end_c, color]

    # 2차원 리스트 생성
    arr = [[0] * 10 for _ in range(10)]
    # print(arr)

    # 보라색 칸의 수
    result = 0

    # rectangle_list를 순회하면서 star_r~end_r, start_c~end_c 돌면서 색깔 입히기
    for i in range(N):
        # 그릴 사각형 정보 받아 오기
        start_r = rectangle_list[i][0]
        start_c = rectangle_list[i][1]
        end_r = rectangle_list[i][2]
        end_c = rectangle_list[i][3]
        color = rectangle_list[i][4]
        #print(start_r, start_c, end_r, end_c, color)
        # 사각형 정보 바탕으로 색깔 바꾸기
        for r in range(end_r - start_r + 1): # end가 start보다 큼
            for c in range(end_c - start_c + 1):
                # 다른 색이 칠해져 있을 수 있음
                if (color == 1 and arr[start_r + r][start_c + c] == 2) \
                        or (color == 2 and arr[start_r + r][start_c + c] == 1):
                    # 처음 보라색이 된 거라면(보라색 위치에 한 번 더 올 수도 있으니까)
                    if arr[start_r + r][start_c + c] != 3:
                        result += 1 # 보라색 count + 1
                    arr[start_r + r][start_c + c] = 3
                else:
                    arr[start_r + r][start_c + c] = color # 색칠하기

        # # 현재 상태 출력하기
        # for x in range(N):
        #     print(arr[x])


    # for r in range(10): # 10x10 이니까 10번씩 반복
    #     for c in range(10):
    #         if arr[r][c] == 3:
    #             result += 1

    print(f'#{test_case} {result}')