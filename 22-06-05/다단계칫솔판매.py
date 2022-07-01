# https://programmers.co.kr/learn/courses/30/lessons/77486

from collections import defaultdict
answer, answer_dic, enroll_dic = [], defaultdict(int), defaultdict(str)


def give_money(now, now_money):
    if now == "-" or now_money < 1:
        return
    answer_dic[now] += now_money - (now_money // 10)
    give_money(enroll_dic[now], (now_money // 10))


def solution(enroll, referral, seller, amount):

    for e_idx, person in enumerate(enroll):
        enroll_dic[person] += referral[e_idx]
    for s_idx, sell in enumerate(seller):
        give_money(sell, amount[s_idx] * 100)

    for person in enroll:
        answer.append(answer_dic[person])

    return answer
