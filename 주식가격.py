from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        time = 0
        price = prices.popleft()
        for i in prices:
            time+=1
            if price > i:
                break
        answer.append(time)
    #print(answer)
    return answer
solution([1, 2, 3, 2, 3])