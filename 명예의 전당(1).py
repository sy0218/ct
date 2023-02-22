def solution(k, score):
    answer = []
    result = []
    for i in score:
        answer.sort()

        if len(answer) == k:
            if min(answer) < i:
                answer[answer.index(min(answer))] = i
        else:
            answer.append(i)
        result.append(min(answer))

    return result

solution(3,[10, 100, 20, 150, 1, 100, 200])
