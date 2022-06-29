# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]
    words_set = set()
    last = ""
    for idx, word in enumerate(words):
        if idx == 0:
            last = word[-1]
            words_set.add(word)
            continue
        loop = (idx // n) + 1
        order = (idx % n) + 1
        if word.startswith(last) == True:
            last = word[-1]
            prev_len = len(words_set)
            words_set.add(word)
            if len(words_set) == prev_len:
                answer = [order, loop]
                break
        else:
            answer[0], answer[1] = order, loop
            break
    return answer
