def solution(s):
    answer = ''
    s = s.lower()
    if s.count('p') == s.count('y'):
        answer = True
    else:
        answer = False
    #print(s.count('p'))
    print(answer)
    return answer
solution("Pyy")