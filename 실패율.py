def solution(N, stages):
    fail = {}
    all = len(stages)
    for i in range(1,N+1):
        stages.count(i) #미클리어 카운트

        if all == 0:#스테이지에 도달한 플레이어수가 없을떄
            fail[i] = 0
        else:
            fail[i] = (stages.count(i)/all)
            all -= stages.count(i)
        
    print(fail)

    #value 기준 정렬 & key값 출력
    #dict = sorted(dict, key=dict.get)
    s = sorted(fail,key = fail.get, reverse = True)
    return s

print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))
