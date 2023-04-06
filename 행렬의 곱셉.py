
def solution(arr1, arr2):
    answer=[]
    #arr1 행렬을 하나씩 꺼냄
    for i in arr1:
        #print(i)
        list = []

        #arr2행렬과 arr1행렬을 곱해줌
        #arr2[0]길이만큼
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(i)):
                total+=i[k]*arr2[k][j]
            list.append(total)
        answer.append(list)

    print(answer)   
    return answer
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
         [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
'''

list = [[1,2],[3,4],[]]
'''