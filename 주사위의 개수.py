def solution(box, n):
    answer = 0
    a = box[0]//n
    b = box[1]//n
    height = box[2]//n
    answer = a*b*height 
    return answer

print(solution([10, 8, 6], 3))