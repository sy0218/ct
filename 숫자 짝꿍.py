
def solution(X, Y):
    answer = ''
    #0~9까지 딕셔너리 만들기
    x_dict = {str(i):0 for i in range(10)}
    y_dict = {str(i):0 for i in range(10)}
    
    #X에 있는 값 딕셔너리에서 증감시켜주기 
    for i in X:
        x_dict[i] += 1
    #print(x_dict)

    #Y에 있는 값 딕셔너리에서 증감시켜주기 
    for i in Y:
        y_dict[i] += 1
    #print(y_dict)

    
    for i in range(9,-1,-1):
        num = min(x_dict[str(i)],y_dict[str(i)])
        #print(num)
        if answer=='' and i==0 and num!=0:
            return '0'
        
        if num == 0:
            continue
        else:
            answer += str(i)*num

    if answer == '':
        return '-1'
    else:
        #print(answer)
        return answer
    
solution("100", "203045")

'''
x='123'
y="123450"

for i in x:
    if i in y:
        y = y.replace(i,'',1)
print(y)
'''

