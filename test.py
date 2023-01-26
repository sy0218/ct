def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    while budget < sum(d):
        d.pop()
    print(len(d))
    return len(d)
solution([2,2,3,3],10)