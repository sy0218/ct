def solution(n,left,right):
    answer = []
    for i in range(left, right+1):
        a=i//n
        b=i%n
        answer.append(max(a,b)+1)
    print(answer)
    return answer
solution(3,2,5)

