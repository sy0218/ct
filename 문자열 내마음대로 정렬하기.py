def solution(strings, n):
    answer = []
    new_list = []
    for i in strings:
        new_list.append(i[n]+i)
    new_list.sort()

    for i in new_list:
        answer.append(i[1:])
    print(answer)
    return answer

solution(["sun", "bed", "car"],1)
