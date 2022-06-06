# https://programmers.co.kr/learn/courses/30/lessons/92341
import math
last_time = 1, 439


def calc_price(fees, total_minute):
    default_time, default_price, per_time, per_price = fees
    return default_price + math.ceil((total_minute - default_time) / per_time) * per_price


def solution(fees, records):
    car_dict = dict()
    # 기본 시간, 기본 요금, 단위 시간, 단위 시간 당 요금
    answer = []
    # 출차 내역 없으면 무조건 23:59 출차
    result_dict = dict()
    for record in records:
        time, car_num, status = record.split(" ")
        hour, minute = time.split(":")
        total_minute = int(hour) * 60 + int(minute)

        if status == "OUT":
            if result_dict.get(car_num):
                result_dict[car_num] = total_minute - \
                    car_dict.get((car_num, "IN")) + result_dict.get(car_num)
            else:
                result_dict[car_num] = total_minute - \
                    car_dict.get((car_num, "IN"))
            car_dict.pop((car_num, "IN"))
        else:
            car_dict[(car_num, status)] = total_minute
    for left_car_num, in_time in car_dict.items():
        print(left_car_num, in_time)
        if result_dict.get(left_car_num[0]):
            result_dict[left_car_num[0]] = last_time - \
                in_time + result_dict.get(left_car_num[0])
        else:
            result_dict[left_car_num[0]] = last_time - in_time
    print(result_dict)
    return answer
