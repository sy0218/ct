def solution(d, budget):
    answer = 0
    total_budget = 0
    while True:
        if len(d) == 0 or (total_budget + min(d)) > budget:
            break
        elif total_budget + min(d) <= budget:
            total_budget+=min(d)
            answer += 1
            d.remove(min(d))
    print(answer)
    return answer
solution([1,3,2,5,4],9)