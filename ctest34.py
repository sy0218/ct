def solution(n):
    answer = 0
    if n**0.5 == int(n**0.5):
        answer = 1
    else:
        answer = 2
    print(answer)
    return answer

solution(144)