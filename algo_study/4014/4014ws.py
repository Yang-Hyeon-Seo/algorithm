'''
반례 찾다가 맞는지 확인하기 위해 우성님 코드 가져옴
'''
import sys
sys.stdin = open('input.txt')

# 활주로 건설 가능 여부를 판단하는 함수
def runway_available(arr):
    global ans

    # info or info_r 순회
    for r in range(N):
        check_row = arr[r]      # 현재 행
        visited = [False] * N   # 경사로가 이미 설치된 위치 표시
        idx = 0                 # 비교 기준이 되는 인덱스 (현재 높이 기준)

        # 현재 행의 두 번째 칸부터 끝까지 순회
        for c in range(1, N):

            # 아직 경사로가 설치되지 않은 칸일 때만 검사
            if not visited[c]:

                # 1. 현재 칸이 이전 칸보다 1 높을 때 (오르막)
                if check_row[idx] + 1 == check_row[c]:
                    # 오르막 경사로를 놓을 수 있는지 검사
                    # 기준 idx 로부터 뒤쪽 x칸이 모두 같은 높이여야 함
                    # 또한 이미 경사로가 설치된 적이 없어야 함

                    # 1.1 설치 불가능한 경우 (길이 부족 or 이미 경사로 있음)
                    if idx + 1 < X or True in visited[idx - X + 1: idx + 1]:
                        break
                    # 1.2 설치 가능한 경우
                    else:
                        # 경사로 설치 -> idx 기준으로 x칸을 True 표시
                        for i in range(idx - X + 1, idx + 1):
                            visited[i] = True
                        idx = c     # 기준 위치를 현재 칸으로 변경

                # 2. 현재 칸이 이전 칸보다 1 낮을 때 (내리막)
                elif check_row[idx] - 1 == check_row[c]:

                    # 내리막은 앞으로 x칸이 모두 같은 높이여야 설치 가능
                    # 2.1 조건을 만족하면 그 구간에 경사로 설치
                    if len(set(check_row[c:c + X])) == 1 and len(check_row[c:c + X]) == X:
                        for i in range(c, c + X):
                            if 0 <= i < N:
                                visited[i] = True
                        idx = c     # 기준 위치를 현재 칸으로 변경
                    # 2.2 경사로를 높을 수 없으면 종료
                    else:
                        break

                # 3. 현재 칸의 높이가 이전 칸과 같을 때 (평지)
                elif check_row[idx] == check_row[c]:
                    idx = c     # 기준 위치를 현재 칸으로 이동

                # 4. 높이 차이가 2 이상이면 활주로 불가하므로 반복 종료
                else:
                    break
        # for 문이 정상 종료 된 경우
        else:
            ans += 1    # 활주로 가능 개수 + 1


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())    # N: 지도 크기, X: 경사로 길이
    info = [list(map(int, input().split())) for _ in range(N)]  # 높이 정보
    info_r = list(map(list, zip(*info)))    # 높이 정보를 전치시킴

    ans = 0     # 활주로 가능 개수 초기화
    runway_available(info)      # 가로 방향 검사
    runway_available(info_r)    # 세로 방향 검사

    print(f"#{tc} {ans}")