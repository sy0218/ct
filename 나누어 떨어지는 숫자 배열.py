def solution(array, divisor):
    answer = []
    for i in array:
        if i%divisor==0:
            answer.append(i)
    answer.sort()
    
    if len(answer) == 0:
        return [-1]
    else:            
        return answer
        
print(solution([3,2,6],10))