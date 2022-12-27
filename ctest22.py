def solution(num_list):
    answer = [0,0]
    for i in num_list:
        if i%2 == 0:
            answer[0] = answer[0]+1
        else:
            answer[1] = answer[1]+1
    print(answer)
    return answer

solution([1,2,3,4,5])