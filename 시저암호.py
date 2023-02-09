
list = 'abcdefghijklmnopqrstuvwxyz'
big_list = 'ABCDEFGHIZKLMNOPQRSTUVWXYZ'
print(list.index('z'))

def solution(s,n):
    answer = ''
    for i in s:
        if i.islower():
            answer += list[(list.index(i)+n)%26]
        elif i.isupper():
            answer += list[(list.index(i.lower())+n)%26].upper()
        else:
            answer += ' '
        
    return answer
print(solution('a B z',4))

