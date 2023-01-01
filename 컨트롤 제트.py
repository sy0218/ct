def solution(my_string):
    answer = 0
    my_string_list = my_string.split(' ')
    for i in range(len(my_string_list)):
        if my_string_list[i] != 'Z':
            answer += int(my_string_list[i])
        else:
            answer -= int(my_string_list[i-1])
    print(answer)
    return answer
solution("1 2 Z 3")