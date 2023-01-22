def solution(left, right):
    answer = 0
    divisorsList = []
    for i in range(left, right+1):
        for k in range(1, int(i**(1/2)) + 1):
            if (i % k == 0):
                divisorsList.append(k) 
                if ( (k**2) != i) : 
                    divisorsList.append(i // k)
        if len(divisorsList)%2 == 0:
            answer += i
        else:
            answer -= i   
        divisorsList.clear()
    print(answer)        
    return answer
solution(24, 27)

