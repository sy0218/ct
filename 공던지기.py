def solution(numbers,k):
    answer = 1
    for i in range(1,k):
        answer += 2
        if answer > len(numbers):
            answer -=len(numbers)
    return answer
print(solution([1,2,3,4],2))
