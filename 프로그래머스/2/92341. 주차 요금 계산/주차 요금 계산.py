import math

def solution(fees, records):
    answer = []
    
    basic_time = fees[0]
    basic_fee = fees[1]

    unit_time = fees[2]
    unit_fee = fees[3]

    now_car = []
    car = dict()
    fee = dict()
    time = dict()
        
    for ele in records:
        tmp = list(ele.split())
        if tmp[2] == 'IN':
            now_car.append(tmp[1])
            car[tmp[1]] = tmp[0]
            
            if tmp[1] not in fee:
                fee[tmp[1]] = 0
                
            if tmp[1] not in time:
                time[tmp[1]] = -basic_time
        else:
            now_car.remove(tmp[1])
            
            prev_time = list(map(int, car[tmp[1]].split(':')))
            now_time = list(map(int, tmp[0].split(':')))

            total_time = (now_time[0] * 60 + now_time[1]) - (prev_time[0] * 60 + prev_time[1])
            time[tmp[1]] += total_time

    for ele in now_car:
        prev_time = list(map(int, car[ele].split(':')))
        
        total_time = (23 * 60 + 59) - (prev_time[0] * 60 + prev_time[1])
        time[ele] += total_time

    for ele in time.keys():
        if time[ele] < 0:
            if time[ele] == -basic_time:
                continue
            fee[ele] += basic_fee
        else:
            fee[ele] += basic_fee + math.ceil(time[ele] / unit_time) * unit_fee

    key = sorted(fee.keys())

    for ele in key:
        answer.append(fee[ele])

    return answer