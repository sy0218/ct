def ft(n):
    factory = 1
    for i in range(1,n+1):
        factory *=i
    return factory

def solution(n):
    answer = 0
    while ft(answer) <= n:
        answer +=1
    return answer-1
print(solution(3628800))