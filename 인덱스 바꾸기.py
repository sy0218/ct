def solution(my_string, num1, num2):
    answer = ''
    for i in my_string:
        answer += i
    answer_list = list(answer)
    answer_list[num1], answer_list[num2] = answer_list[num2], answer_list[num1]
    answer = ''.join(answer_list)
    return answer

print(solution('hello',1,2))