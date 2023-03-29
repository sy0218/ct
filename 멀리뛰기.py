#1칸이면 1개
#2칸이면 2개
#3칸이면 3개
#4칸이면 5개
#5칸이면 8개
#오 규칙이 보인다!!!

def solution(n):
    answer = 0
    if n==1:
        return 1
    elif n==2:
        return 2
    
    list = [0]*n
    list[0] = 1
    list[1] = 2
    
    for i in range(2,n):
        list[i] = list[i-2]+list[i-1]
    
    answer = list[-1]%1234567
    return answer
solution(4)