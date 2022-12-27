def solution(numbers):
    answer = 0
    for i in numbers:
        answer = answer + i
    answer = answer / len(numbers)
    print(answer)
    return answer

solution([1,2,3,4,5,6,7,8,9,10])