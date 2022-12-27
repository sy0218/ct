def solution(n):
    answer = 0
    for i in str(n):
        answer = answer + int(i)
    print(answer)
    return answer

solution(1234)