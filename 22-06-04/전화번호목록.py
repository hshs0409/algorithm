def solution(phone_book):
    phone_dict = dict()
    phone_book.sort()
    for phone in phone_book:
        for p in range(len(phone[:-1])):
            phone_dict[phone[: p + 1]] = True
    answer = True
    for phone in phone_book:
        if phone_dict.get(phone) != None:
            answer = False
    return answer
