def get_final_position(commands):
    # 시작 위치
    r, c = 0, 0

    # 여기에 코드를 작성하세요.
    for direction in commands:
        if direction == 'E':
            c += 1
            pass
        elif direction == 'S':
            r += 1
            pass
        elif direction == 'W':
            c -= 1
            pass
        else:  # direction == 'N'
            r -= 1
            pass
    return r, c

# 테스트
commands = ['E', 'E', 'S', 'W', 'N']
end_r, end_c = get_final_position(commands)
print(f"최종 위치: ({end_r}, {end_c})") # 최종 위치: (0, 1)