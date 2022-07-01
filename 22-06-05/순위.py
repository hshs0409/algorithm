# https://programmers.co.kr/learn/courses/30/lessons/49191

from collections import defaultdict

def solution(n, results):
    answer, win, lose = -0, defaultdict(set), defaultdict(set)
    for winner, loser in results:
        win[winner].add(loser)  # 내가 이긴 애들
        lose[loser].add(winner)  # 내가 진 애들

    for i in range(1, n + 1):
        for loser in win[i]:  # 내가 이긴 애들
            lose[loser].update(lose[i])
        for winner in lose[i]:
            win[winner].update(win[i])
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer
