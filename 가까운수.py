def solution(array, n):
    array.sort()
    answer = array[0]
    for i in array:
        if abs(n-i) < abs(n-answer):
            answer = i    
    return answer
print(solution([-10, -16, 11, 12],-13))