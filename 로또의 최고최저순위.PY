def rank(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    max_score = 0
    min_score = 0

    for i in lottos:
        if i == 0:
            max_score += 1
        elif i in win_nums:
            max_score += 1
            min_score += 1        

    answer.append(rank(max_score))
    answer.append(rank(min_score))

    print(answer)
    return answer
solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25])