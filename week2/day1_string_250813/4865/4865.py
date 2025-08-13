"""
4865_글자수
두 개의 문자열 str1, str2가 주어짐
str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고
그 중에 가장 많은 글자의 개수를 출력하는 프로그램 만들기

파이썬의 경우 딕셔너리 사용 가능
"""

# 아이디어
"""
딕셔너리 사용하기(아직 안 친하니까)
함수로 만들기(함수 연습)

str1을 순회하면서 key값이 없으면 추가하기(함수 있었는데 뭐였더라)

그리고 key값 하나씩 받아서 str2 순회하면서
동일한 값 있으면 value + 1

순회 끝나고 나서 딕셔너리 돌면서 value 가장 큰 거 찾아서
return 해당 키값

만약 딕셔너리를 사용하지 못한다면, list 만들어서 했을것같음
"""

import sys
sys.stdin = open('sample_input.txt')


# 딕셔너리 만드는 함수
def make_dictionary(arr):
    """
    딕셔너리 만드는 함수
    arr 입력 받아서 각 값에 대해 value는 0인 딕셔너리 만들어서 리턴
    """
    dictionary = {}
    for key in arr:  # arr 순회
        dictionary.setdefault(key, 0)  # key가 있으면 넘어가고, 없으면 0으로 초기화하는 함수
    return dictionary


# 딕셔너리 입력 받아서 key값이 있으면 value + 1하는 함수 만들기
def count_char(string, dictionary):
    """
    string과 dictionary 입력 받아서 dictionary의 키 안에 있는 문자가 string 안에 몇 개 있는지 세는 함수
    :param string: 문자를 셀 문자열
    :param dictionary: 문자의 수를 저장할 딕셔너리
    :return: 딕셔너리 리턴
    """
    for character in string:  # 문자열 안의 문자 각각을 받음
        if character in dictionary:  # 딕셔너리 안에 있다면
            dictionary[character] += 1  # 값을 하나 늘림

    return dictionary


# 딕셔너리 안에서 가장 큰 수 찾는 함수
def find_max_number(dictionary):
    """
    딕셔너리의 키 중 가장 큰 값을 찾는 함수
    item 함수 활용하기
    가장 큰 값 리턴

    max_char이 필요한 건 아니지만, items()함수 연습해보려고 사용해봄
    """
    max_char, max_num = '', 0
    for character, number in dictionary.items():
        if max_num < number:
            max_num = number  # 만약 max_num 보다 현재 number가 더 크다면 max_number 갱신
            max_char = character

    return max_char, max_num
    # # char 리턴 안 할 경우
    # for number in dictionary.values():
    #     if max_num < number:
    #         max_num = number  # 만약 max_num 보다 현재 number가 더 크다면 max_number 갱신

# 입력 받기
T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    character_dictionary = make_dictionary(str1)  # 딕셔너리 생성
    character_dictionary = count_char(str2, character_dictionary)  # 숫자 카운트
    max_char, max_num = find_max_number(character_dictionary)  # 가장 큰 value 리턴

    print(f'#{test_case} {max_num}')