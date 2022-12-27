food = 12000
drink = 2000

def solution(n, k):
    answer = 0
    answer = (food*n)+(drink*k)
    if n/10 >= 1:
        answer = answer-(int(n/10)*2000)
    print(answer)
    return answer

solution(10,3)