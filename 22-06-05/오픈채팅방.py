def solution(records):
    id_dict, log_arr = dict(), []
    for record in records:
        splited = record.split(" ")
        if splited[0] == "Enter":
            id_dict[splited[1]] = splited[2]
            log_arr.append(f'{splited[1]}님이 들어왔습니다.')
        elif splited[0] == "Leave":
            log_arr.append(f'{splited[1]}님이 나갔습니다.')
        else:
            id_dict[splited[1]] = splited[2]

    for log_idx, log in enumerate(log_arr):
        idx = log.index("님")
        log_arr[log_idx] = log.replace(log[:idx], id_dict[log[:idx]])

    return log_arr
