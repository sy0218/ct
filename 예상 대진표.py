
def solution(N,A,B):
    answer = 1
    while True:
        A = (A//2)+(A%2)
        B = (B//2)+(B%2)
        
        if A==B:
            break

        answer += 1
    print(answer)
    return answer
solution(8,4,7)
