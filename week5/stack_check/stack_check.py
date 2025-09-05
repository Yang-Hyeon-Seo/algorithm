import sys
sys.stdin = open('input.txt')


def check_brackets_no_dict(string):
    N = len(string)

    # print(string, N)

    s = [0] * N  # N크기의 스택 생성
    top = -1  # 제일 위 가리킴
    for i in range(N):
        # print(string[i], s, top)
        if string[i] in ['(', '{', '[']:
            top += 1
            s[top] = string[i]  # 현재 괄호 저장\
        elif string[i] in [')', '}', ']']:
            # 닫힌 괄호 만나면 짝꿍인지 확인하고, 짝꿍이 아니라면 틀림
            if top < 0:
                # 빈 스택이라면 짝꿍이 없음
                # print('빈스택')
                return -1
            elif string[i] == ')' and s[top] == '(':
                # 짝꿍임, pop()
                # print('()')
                top -= 1
            elif string[i] == '}' and s[top] == '{':
                # print('{}')
                top -= 1
            elif string[i] == ']' and s[top] == '[':
                # print('[]')
                top -= 1
            else:
                # 짝꿍이 아님
                return -1
    # 끝까지 돌았다면 ture인데
    # 스택에 남아있는게 있다면 false
    if top >= 0:
        return -1
    return 1


T = int(input().strip())
for tc in range(1, T + 1):
    line = input().strip()
    result = check_brackets_no_dict(line)
    print(f'#{tc} {result}')