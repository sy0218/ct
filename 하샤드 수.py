def num_sum(x):
    answer = 0
    for i in str(x):
        answer += int(i)
    return answer

def solution(x):
    answer = ''
    if x%num_sum(x) == 0:
        answer = True
    else:
        answer = False
    print(answer)
    return answer
solution(11)