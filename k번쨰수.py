def solution(array, commands):
    answer = []
    for i in commands:
        new_list = array[i[0]-1:i[1]]
        new_list.sort()
        #print(new_list)
        answer.append(new_list[i[2]-1])
    print(answer)
    return answer
solution([1,5,2,6,3],[[2,5,3],[4,4,1],[1,7,3]])