def solution(price):
    answer = 0
    if price < 100000:
        answer = price
    elif 100000 <= price < 300000:
        answer = int(price*0.95)
    elif 300000 <= price < 500000:
        answer = int(price*0.90)
    else:
        answer = int(price*0.80)
    print(answer)
    return answer

solution(580000)