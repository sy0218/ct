def solution(progresses, speeds):
    answer = []

    #리스트가 있으면 반복
    while progresses:
        
        #업데이트 해줌
        for i in range(len(progresses)):
            progresses[i] = progresses[i]+speeds[i]

        #progresses[0]이 100보다 크면 배포
        num = 0
        while progresses and progresses[0]>=100:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                num+=1
            answer.append(num)
    

    print(answer)
    return answer 
solution([93, 30, 55],	[1, 30, 5])