'''a=['1','2','a']
for i in a:
    if i.isdigit() == True:
        print('o')
    else:
        print('x')'''

a = ['zero','one','two','three','four','five','six','seven','eight','nine']
def solution(s):
    answer = ''
    alp = ''
    for i in s:
        if i.isdigit():
            answer += str(i)
        elif i.isalpha():
            alp += i
            if alp in a:
                answer += str(a.index(alp))
                alp = ''
            

    return int(answer)
print(solution("23four5six7"))


