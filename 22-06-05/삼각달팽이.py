# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    snail = [[0] * (i + 1) for i in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:  # left down
                x += 1
            elif i % 3 == 1:  # right
                y += 1
            elif i % 3 == 2:  # left up
                x -= 1
                y -= 1
            snail[x][y] = num
            num += 1
    return [element for answer in snail for element in answer]
