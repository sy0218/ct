def solution(n):
    answer = 0
    if n<7:
        answer = 1
    elif n%7 == 0:
        answer = n/7
    elif n%7 != 0:
        answer = int(n/7)+1
    print(answer)
    return answer

solution(15)