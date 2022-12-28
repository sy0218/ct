import re
def solution(my_string):
    answer = []
    num_string = re.sub(r'[^0-9]', '', my_string)#문자열 에서 숫자아닌 것 공백처리
    for i in num_string:
        answer.append(int(i))
    answer.sort()
    return answer

print(solution('hi12392'))