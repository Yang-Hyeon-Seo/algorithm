string = '( )( )((( )))'

answer = 0  # 결과 저장
N = 100
stack = [0] * N  # 적당히 긴 스택 생성
top = -1
for i in string:
  if i == '(':
    top += 1
    if top < N:
      stack[top] = i
    else:
      print('overflow')
      answer = 1  # 오버플로우 -> 1
      break
  elif i == ')':
    top -= 1
    if top < -1:
      print('underflow')
      answer = -1  # 언더플로우 -> -1
      break
    else:
      print(stack[top + 1])
else:  # break가 아닌 경우에
  if top != -1:  # stack에 남은게 있다면
    answer = 1  # 남은게 있음 -> 오류
print(top)
print(answer)