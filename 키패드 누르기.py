def solution(numbers, hand):
    answer = ''
    num_dic = {1:[0,0], 2:[0,1], 3:[0,2],
               4:[1,0], 5:[1,1], 6:[1,2],
               7:[2,0], 8:[2,1], 9:[2,2],
               '*':[3,0], 0:[3,1], '#':[3,2]}
    
    L_point = num_dic['*']
    R_point = num_dic['#']

    #print(L_point)
    #print(R_point)
    for i in numbers:
        now_point = num_dic[i]
        if i==1 or i==4 or i==7 or i=='*':
            answer += 'L'
            L_point = now_point
        elif i==3 or i==6 or i==9 or i=='#':
            answer+='R'
            R_point = now_point
        else:
            L_dis = abs(L_point[0]-now_point[0])+abs(L_point[1]-now_point[1])
            R_dis = abs(R_point[0]-now_point[0])+abs(R_point[1]-now_point[1])
            
            if L_dis == R_dis:
                if hand == 'right':
                    answer += 'R'
                    R_point = now_point
                else:
                    answer += 'L'
                    L_point = now_point
            elif L_dis < R_dis:
                answer += 'L'
                L_point = now_point
            else:
                answer += 'R'
                R_point = now_point

                
    print(answer)
    return answer
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'right')