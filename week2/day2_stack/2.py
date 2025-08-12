# string = '( )( )((( )))'

import sys
sys.stdin = open('input_2.txt')

T = int(input())
for test_case in range(1, T + 1):
  string = input()

  answer = 1  # 결과 저장 / 정상 종료 1 / 비정상 종료 -1
  N = 100
  stack = [0] * N  # 적당히 긴 스택 생성
  top = -1
  for i in string:
    if i == '(':
      # push
      top += 1
      if top < N:
        stack[top] = i
      else:
        #print('overflow')
        answer = -1  # 오버플로우 -> 1
        break

    elif i == ')':
      # pop
      top -= 1
      if top < -1:
        #print('underflow')
        answer = -1  # 언더플로우 -> -1
        break
      else:
        pop_result = stack[top + 1]
  else:  # break가 아닌 경우에
    if top != -1:  # stack에 남은게 있다면
      answer = -1  # 남은게 있음 -> 오류
  # #print(top)
  print(answer)
  #
  # # 빈 리스트 생성
  # stack = []
  #
  # def push(item):
  #   stack.append(item)
  #
  # push(3)