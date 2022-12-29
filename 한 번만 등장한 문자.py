def solution(s):
    answer = s
    for i in s:
        if answer.count(i) >= 2:
            answer = answer.replace(i,'')
    answer = ''.join(sorted(answer))
    return answer
print(solution('hello'))