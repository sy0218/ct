def solution(dartResult):
    answer = 0
    str = ''
    new = []
    answer_list = []
    for i in dartResult:
        str += i 
        if i=='D'or i=='#' or i=='S' or i=='*' or i=='T':
            new.append(str)
            str = ''

    for i in range(len(new)):
        #print(new[i])

        if 'S' in new[i]:
            answer_list.append(int(new[i][0:-1])**1)
        
        elif 'D' in new[i]:
            answer_list.append(int(new[i][0:-1])**2)

        elif 'T' in new[i]:
            answer_list.append(int(new[i][0:-1])**3)

        elif '#' in new[i]:
            answer_list[-1] = answer_list[-1]*-1

        elif '*' in new[i]:
            if len(answer_list) <= 1:
                answer_list[-1] = answer_list[-1]*2
            else:
                answer_list[-1] = answer_list[-1]*2
                answer_list[-2] = answer_list[-2]*2

    answer = sum(answer_list)
    return answer
solution('1D2S#10S')






