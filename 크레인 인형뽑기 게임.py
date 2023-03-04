def solution(board, moves):
    answer = 0
    box = []
    for i in moves:
        for j in board:
            #print(j[i-1])
            if j[i-1] != 0:
                box.append(j[i-1])
                j[i-1] = 0
                break
        
        if len(box)>1 and box[-1]==box[-2]:
            del box[-1]
            del box[-1]
            answer+=2        
    print(answer)    
    return answer
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
         [1,5,3,5,1,2,1,4])