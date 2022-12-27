def solution(my_string):
    f_string = ['a','e','i','o','u']
    answer = ''
    for i in my_string:
        if i in f_string:
            continue
        else:
            answer = answer + i
    print(answer)
    return answer

solution('bus')