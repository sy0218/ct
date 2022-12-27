def solution(my_string):
    answer = ''
    my_string_list = list(my_string)
    my_string_list.reverse()
    answer=''.join(my_string_list)
    print(answer)
    return answer

solution('jaron')