import math
def solution(denum1, num1, denum2, num2):
    answer = [0,0]
    answer[1] = num1*num2
    answer[0] = denum1*num2 + denum2*num1

    a = math.gcd(answer[1],answer[0])
    answer[0] //= a
    answer[1] //= a

    print(answer)
    return answer

solution(9,2,1,3)