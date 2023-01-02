def solution(array):
    answer = 0
    array_count=0
    for i in array:
        if array.count(i) > array_count:
            array_count = array.count(i)
            answer = i
            
    array.remove(answer)

    for i in list(set(array)):
        if array.count(i) == array_count:
            answer = -1
    print(answer)
    return answer
solution([1,1,2,2,3,3,3])