def solution(sides):
    answer = 0
    max_num = max(sides)
    sides.remove(max_num)
    if max_num >= sum(sides):
        answer = 2
    else:
        answer = 1
    print(answer)
    return answer

solution([1,2,3])