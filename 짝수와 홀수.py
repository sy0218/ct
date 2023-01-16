def solution(num):
    answer = ''
    if num%2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    print(answer)
    return answer
solution(3)