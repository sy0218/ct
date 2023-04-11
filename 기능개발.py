
def solution(progresses,speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] = progresses[i]+speeds[i]

        num=0
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            num+=1
    
        if num!=0:
            answer.append(num)

    print(answer)
    return answer 
solution([93, 30, 55],[1,30,5])


