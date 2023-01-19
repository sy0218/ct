def solution(numbers):
    answer = 0
    for i in range(10):
        try:
            numbers.index(i)
        except ValueError:
            answer += i
    '''for i in range(10):
        if numbers.find(i) == -1: #배열에 없으면
            answer += i'''
    print(answer)
    return answer
solution([1,2,3,4,6,7,8,0])