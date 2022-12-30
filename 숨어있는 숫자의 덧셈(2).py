import re
def solution(my_string):
    answer = 0
    num_list = re.findall('\d+',my_string)#문자열에서 숫자만
    for i in num_list:
        answer += int(i)

    return answer
print(solution('aAb1B2cC34oOp'))