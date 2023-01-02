def solution(polynomial):
    
    polynomial = polynomial.replace(' ','')
    polynomial = polynomial.split('+')
    x=0
    num=0
    for i in polynomial:
        
        if i.isnumeric(): #숫자 경우
            num += int(i)
        else: #숫자 아닐 경우
            if i=='x': #x이면 +1
                x += 1
            else: #아니면 x빼고 슬라이싱 ex)7x면 7
                x += int(i[:-1])
        
    if x==1:#x가 1이면 공백으로 줌
        x=''
    
    if x==0 and num ==0: #둘다 0이면 공백 리턴
        return ''
    if x==0 and num !=0: #x가 0이면 num리턴
        return str(num)
    if x!=0 and num==0: #num이 0이면 일차항 리턴
        return str(x) + 'x'
    
    return str(x) + 'x + ' + str(num)
        
print(solution("x + x + 7 + 9"))