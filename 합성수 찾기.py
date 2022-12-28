def solution(n):
    answer = 0
    for i in range(1,n+1):
        new_list = []
        for j in range(1,i+1):
            if i%j == 0:
                new_list.append(j)
        if len(new_list)>=3:
            answer+=1
    return answer

print(solution(10))