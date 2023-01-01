from math import gcd
#gcd는 최대 공약수를 의미
def solution(a,b):
    answer = 0
    b//=gcd(a,b)
    print(b)
    while b%2==0 or b%5==0:
        if b%2==0:
            b//=2
        elif b%5==0:
            b//=5
    if b==1:
        answer=1
    else:
        answer=2
    return answer
print(solution(10,100))