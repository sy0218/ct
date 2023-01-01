def solution(dots):
    answer = 0
    first = dots[0]
    for i in dots:
        if first[0] != i[0] and first[1] != i[1]:
            answer = abs(i[0]-first[0])* abs(i[1]-first[1])
    print(answer)
    return answer
solution([[-1, -1], [1, 1], [1, -1], [-1, 1]])