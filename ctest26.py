def solution(n):
    answer = []
    for i in range(1,n+1):
        if i%2 != 0:
            answer.append(i)
        else:
            continue
    print(answer)
    return answer

solution(15)