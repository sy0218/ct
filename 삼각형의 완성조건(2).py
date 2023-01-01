def solution(sides):
    answer = 0
    number = max(sides)-min(sides)+1
    for i in range(max(sides),sum(sides)):
        answer += 1
    while True:
        if number == max(sides):
            break
        else:
            number += 1
            answer += 1
    print(answer)
    return answer
solution([11, 7])