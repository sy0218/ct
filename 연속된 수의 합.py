import math
def solution(num, total):
    answer = []
    print(math.ceil(total/num))
    print(num//2)
    if num%2 !=0:
        for i in range(num):
            if i == num//2:
                answer.append(total//num)
            else:
                answer.append((total//num)-(num//2-i))
    else:
        for i in range(num):
            if i == num//2:
                answer.append(math.ceil(total/num))
            else:
                answer.append(math.ceil(total/num)-(num//2-i))
    print(answer)
    return answer
solution(4,14)