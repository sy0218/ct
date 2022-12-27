def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer = answer + n*i
    print(answer)
    return answer

solution('hello',3)