def solution(n):
    piz = 6
    while True:
        if piz%n == 0:
            break
        else:
            piz += 6
    return piz//6

print(solution(10))