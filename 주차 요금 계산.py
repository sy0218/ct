import math

def solution(fees, records):
    answer = []
    car_total_time = {}
    for i in records:
        if i.split(' ')[1] not in car_total_time:
            car_total_time[i.split(' ')[1]] = 0
    #차량번호로 정렬
    car_total_time = dict(sorted(car_total_time.items(), key=lambda x: x[0]))
    print(car_total_time)


    in_out = {}
    for i in records:
        if i.split(' ')[2] == 'IN':
            in_out[i.split(' ')[1]] = i.split(' ')[0]
        #아웃이면
        else:
            time = int(i.split(' ')[0].split(':')[0]) - int(in_out[i.split(' ')[1]].split(':')[0])
            min = int(i.split(' ')[0].split(':')[1]) - int(in_out[i.split(' ')[1]].split(':')[1])
            del in_out[i.split(' ')[1]]
            car_total_time[i.split(' ')[1]] += (time*60)+min

    #입차이후 출차내역이 없으면
    for i in in_out:
        time = 23 - int(in_out[i].split(':')[0])
        min = 59 - int(in_out[i].split(':')[1])
        car_total_time[i] += (time*60)+min
    
    #print(car_total_time)
    for i in car_total_time:
        if car_total_time[i] > fees[0]:
            answer.append(fees[1]+math.ceil((car_total_time[i]-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])
    print(answer)
    return answer
solution([180, 5000, 10, 600],
         ["05:34 5961 IN", 
          "06:00 0000 IN", 
          "06:34 0000 OUT", 
          "07:59 5961 OUT", 
          "07:59 0148 IN", 
          "18:59 0000 IN", 
          "19:09 0148 OUT", 
          "22:59 5961 IN", 
          "23:00 5961 OUT"])

