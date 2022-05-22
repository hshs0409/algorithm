# 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 4 == 3:  # 4로 나눈 나머지가 3일 때
            str1 = "0" + bin(number).split('0b')[1]
            first_index = len(str1) - str1.rindex('0') - 1
            answer.append(number + (2 ** (first_index) - 2 ** (first_index-1)))
        else:
            answer.append(number + 1)
    return answer
