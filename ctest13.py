def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
        else:
            continue
    print(answer)
    return answer

solution([149,180,192,170],167)