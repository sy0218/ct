def solution(array):
    answer = 0
    array.sort()
    answer = array[int(len(array)/2)]
    print(answer)
    return answer

solution([9,-1,0])