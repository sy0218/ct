def solution(n):
    answer = ''
    answer = '수박'*(n//2)+'수'*(n%2)
    print(answer)
    return answer
solution(3)