def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    print(answer)
    return answer
solution([4,7,12],[True,False,True])