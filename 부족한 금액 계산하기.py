def solution(price, money, count):
    num = 1
    for i in range(count):
        money = money - (price*num)
        num += 1
    
    if money >= 0:
        return 0
    else:
        return -money

print(solution(3,20,4))