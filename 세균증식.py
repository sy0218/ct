def solution(n,t):
    answer = n
    for i in range(1,t+1):
        answer = answer*2
    print(answer)
    return answer

solution(7,15)