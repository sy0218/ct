def solution(a,b,n):
    answer = 0
    while n>=a:
        ppp = n%a
        n = (n//a)*b
        answer += n
        n += ppp
    return answer

print(solution(2,1,20))
