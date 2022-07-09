# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    # brown yellow 갯수만 기억
    for x in range(1, yellow + 1):
        y = yellow // x
        if brown + yellow == (x + 2) * (y + 2) and x >= y:
            return [x + 2, y + 2]
