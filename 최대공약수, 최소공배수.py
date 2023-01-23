

def solution(n, m):
    answer = []
    common_divisor = []
    
    for i in range(min(n,m),0,-1):
        if m%i==0 and n%i==0:
            answer.append(i)
            break
    

    for i in range(max(n,m),n*m+1): #최소공배수
        if i%n == 0 and i%m == 0:
            answer.append(i)
            break
    return answer
print(solution(2,5))