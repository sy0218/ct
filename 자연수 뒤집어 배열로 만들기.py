def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    print(answer)
    return answer
solution(12345)