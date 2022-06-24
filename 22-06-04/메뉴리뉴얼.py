from itertools import combinations
from collections import Counter


def solution(orders, courses):
    answer, total_list = [], []
    orders = ["".join(sorted(order)) for order in orders]
    for order in orders:
        for course in courses:
            if course <= len(order):
                for combi in list(combinations(order, course)):
                    total_list.append("".join(combi))
    total_list = Counter(total_list).most_common()
    count_arr = [2 for _ in range(11)]
    for course, count in total_list:
        if max(count_arr[len(course)], count) <= count:
            count_arr[len(course)] = count
            answer.append(course)

    return sorted(answer)
