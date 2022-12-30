import math
def solution(my_str,n):
    answer = []
    num = 0
    num1 = n
    for i in range(math.ceil(len(my_str)/n)):
        answer.append(my_str[num:num1])
        num += n
        num1 += n
    return answer
    
print(solution("abc1Addfggg4556b",6))


