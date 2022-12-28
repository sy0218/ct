def solution(my_string):
    answer =''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i
    answer_list = list(answer)
    answer_list.sort()
    answer = ''.join(answer_list)
    return answer

print(solution('Bcad'))