#순열!!
from itertools import permutations

def solution(k, dungeons):
    answer = 0

    #던전을 순열로 모든 경우의 수를 돌림
    for i in permutations(dungeons):
        print(i)
        #던전의 경우의 수 에서 입장 가능한
        #던전의 수를 확인
        count = 0
        pirodo = k
        for j in i:
            if pirodo >= j[0]:
                count +=1
                pirodo -= j[1]
        if answer < count:
            answer = count
    print(answer)
    return answer
solution(80,[[80,20],[50,40],[30,10]])