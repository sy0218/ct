
def solution(wallpaper):
    answer = []
    fail_index_list = []
    start = []
    end = []
    for i in wallpaper:
        index_list = []
        if '#' in i:
            for j in range(len(i)):
                if i[j] == '#':
                    index_list.append(j)
            fail_index_list.append(index_list)

        else:
            fail_index_list.append(index_list)

    print(fail_index_list)

    for i in range(len(fail_index_list)):
        if len(fail_index_list[i]) != 0:
            answer.append(i)
            break

    max_point = -999
    min_point = 999
    for i in fail_index_list:
        if len(i) == 0:
            continue

        if max(i) > max_point:
            max_point = max(i)        
        if min(i) < min_point:
            min_point = min(i)
    answer.append(min_point)
    #print(min_point)
    #print(max_point)

    for i in range(len(fail_index_list)-1,-1,-1):
        if len(fail_index_list[i]) != 0:
            answer.append(i+1)
            break
    answer.append(max_point+1)
    
    print(answer)
    return answer
solution([".....", "..#..", "....."])

#시작점 = [wallpaper'#'존재하는 인덱스 최솟값,#인덱스 최솟값]
#끝점 = [wallpaper'#'존재하는 인덱스 최대값+1 ,#인덱스 최대값+
