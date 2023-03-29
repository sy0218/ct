'''
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            answer = l-i
            break

    print(answer)
    return answer
solution([3, 0, 6, 1, 5])

'''

def solution(citations):
    citations = sorted(citations)
    print(citations)
    l = len(citations)
    for i in range(l):
        #h번 이상 인용된 논문이 h번 이상
        if citations[i] >= l-i:
            return l-i
    return 0

print(solution([3, 0, 6, 1, 5]))
