def solution(numbers):
    answer = []
    new_answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    #중복제거
    for i in answer:
        if i not in new_answer:
            new_answer.append(i)
    
    #정렬
    new_answer.sort()
    return new_answer

print(solution([5,0,2,7]))