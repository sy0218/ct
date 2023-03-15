def solution(s):
    answer = ''
    s_list = list(map(int,s.split(' ')))
    
    answer += str(min(s_list))
    answer += ' '
    answer += str(max(s_list))

    print(answer)
    return answer
solution("-1 -2 -3 -4")
