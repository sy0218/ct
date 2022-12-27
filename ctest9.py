import math
def solution(num1, num2):
    answer = 0
    answer = math.trunc((num1 / num2)*1000)
    print(answer)
    return answer

solution(3,2)