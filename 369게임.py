def solution(order):
    answer = 0
    for i in str(order):
        for j in range(3,10,3):
            if int(i)==j:
                answer+=1
    return answer

print(solution(133332))