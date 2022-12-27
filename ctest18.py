coffe = 5500

def solution(money):
    answer = []
    answer.append(int(money/coffe))
    answer.append(money-(int(money/coffe)*coffe))
    print(answer)
    return answer

solution(15000)