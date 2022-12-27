def solution(numbers):
    answer = 0
    first_max_number = max(numbers)
    numbers.remove(first_max_number)
    second_max_number = max(numbers)
    answer = first_max_number*second_max_number
    print(answer)
    return answer

solution([1,2,3,4,5])