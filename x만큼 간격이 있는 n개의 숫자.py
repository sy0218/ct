def solution(x, n):
    answer = []
    num = x
    for i in range(n):
        answer.append(num)
        num += x
    print(answer)
    return answer
solution(2,5)