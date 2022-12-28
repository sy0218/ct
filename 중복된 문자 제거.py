from collections import OrderedDict

def solution(my_string):
    answer = ''
    answer = ''.join(OrderedDict.fromkeys(my_string))
    return answer

print(solution("We are the world"))