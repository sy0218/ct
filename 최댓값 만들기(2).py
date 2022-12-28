def solution(numbers):
    answer = answer = numbers[0] * numbers[1]
    for i in range(len(numbers)):
        for j in range(1+i, len(numbers)):
            if numbers[i]*numbers[j] > answer:
                answer = numbers[i]*numbers[j]
    return answer

print(solution([1, 2, -3, 4, -5]))

