
def solution(priorities, location):
    answer = 0

    #[location,중요도] 리스트 만듬
    new_pri = []
    for i in range(len(priorities)):
        new_pri.append([i,priorities[i]])
    print(new_pri)

    #반복문 돌림
    while True:
        #첫문서가 가장높은 중요도가 아닐시
        #맨뒤로 보냄
        if new_pri[0][1] != max(priorities):
            new_pri.append(new_pri[0])
            new_pri.pop(0)

        #첫문서가 가장 높은 중요도이면
        else:
            #중요도 리스트에서 가장높은 중요도 삭제
            priorities.remove(max(priorities))
            #가장높은 중요도 문서와 location이 같으면
            #삭제후 answer+=1해주고 break
            if new_pri[0][0] == location:
                new_pri.pop(0)
                answer+=1
                break
            #가장 높은 중요도 이지만 location과 다르면
            #그냥 삭제후 answer+=1
            else:
                new_pri.pop(0)
                answer+=1
                
    print(answer)
    return answer
solution([1, 1, 9, 1, 1, 1], 0)
