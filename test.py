def solution(X, Y):
    answer = ''
    x_dic = {str(i):0 for i in range(10)}
    y_dic = {str(i):0 for i in range(10)}
    
    
    for i in X:
        x_dic[i] += 1
    for i in Y:
        y_dic[i] += 1
    print(y_dic)
    
    for i in range(9,-1,-1):
        min_num = min(x_dic[str(i)], y_dic[str(i)])
        print(min_num)
        
    return answer
solution("100",	"203045")

