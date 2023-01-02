def solution(polynomial):
    answer =''
    polynomial = polynomial.replace(' ','')
    string = polynomial.split('+')
    x=0
    number=0

    for i in string:
        if 'x' in i:
            if len(i) == 1:
                x+=1
            else:
                if i.split('x')[0] == '-':
                    x -= 1
                else:
                    x += int(i.split('x')[0]) 
        else:
            number += int(i)
    print(x)
    if x!=0 and number!=0:
        if x==1:
            answer = f'x + {number}'
        elif x==-1:
            answer = f'-x + {number}'
        else:
            answer = f'{x}x + {number}'

    elif x==0 and number!=0:
        answer = number
        
    elif x!=0 and number==0:
        if x==1:
            answer='x'
        elif x==-1:
            answer='-x'
        else:
            answer = f'{x}x'
    else:
        answer=''
 
    print(answer)
    return answer
solution("x + -2x + 6")