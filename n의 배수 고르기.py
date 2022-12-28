def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n != 0:
            continue
        else:
            answer.append(i)
    return answer

a = solution(5,	[1, 9, 3, 10, 13, 5])
print(a)
