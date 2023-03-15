def solution(s):
    answer = ''
    answer += s[0].upper()
    
    for i in range(1,len(s)):
        if s[i-1] != ' ':
            answer += s[i].lower()
        else:
            answer += s[i].upper()
    print(answer)
    return answer
solution("3people unFollowed me")
'''

a='s1sd'
if a[0].isdigit():
    print(a)
else:
    a = a[0].upper() + a[1:]
    print(a)
'''