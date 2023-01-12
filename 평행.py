def solution(dost):
    answer = 0
    if (dost[1][1] - dost[0][1])/(dost[1][0] - dost[0][0]) == (dost[3][1]-dost[2][1])/(dost[3][0]-dost[2][0]):
        answer = 1
    elif (dost[2][1] - dost[0][1])/(dost[2][0] - dost[0][0]) == (dost[3][1] - dost[1][1])/(dost[3][0] - dost[1][0]):
        answer = 1
    elif (dost[3][1]-dost[0][1])/(dost[3][0]-dost[0][0]) == (dost[2][1]-dost[1][1]/dost[2][0]-dost[1][0]):
        answer = 1
    print(answer)    
    return answer
solution([[3, 5], [4, 1], [2, 4], [5, 10]])

#평행이기 위한 조건
#1. 두 직선의 기울기가 동일
#2. y절편이 서로 달라야 함
#3. dost[0], dost[1] 과 dost[2], dost[3]
#4. dost[0], dost[2] 과 dost[1], dost[3]
#5. dost[0], dost[3] 과 dost[1], dost[2]