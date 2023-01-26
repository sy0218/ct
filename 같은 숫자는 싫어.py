def solution(arr):
    answer = []
    for i in arr:
        #answer 길이가 0 이거나 i와 answer마지막 값이 같지 않으면 append
        if (len(answer)==0) or (i != answer[-1]):
            answer.append(i)
    return answer
print(solution([1,1,3,3,0,1,1]))