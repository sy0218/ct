def solution(arr1, arr2):
    answer =[]
    for i in range(len(arr1)):
        sum_list =[]
        for k in range(len(arr1[0])):
            sum_list.append(arr1[i][k]+arr2[i][k])
        answer.append(sum_list)
    print(answer)
solution([[1,2],[2,3]],[[3,4],[5,6]])