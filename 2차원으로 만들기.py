def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        a=[]
        for j in range(n):
            a.append(num_list[i])
            i+=1
        answer.append(a)
    return answer

print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))

#이런 방법이 있었구만....
'''def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer'''