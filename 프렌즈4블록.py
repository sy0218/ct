
def solution(m,n,board):
    answer = 0
    rm = set()
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        for i in range(m-1):
            for j in range(n-1):
                now = board[i][j]
                if now == []:
                    continue
                    
                if now == board[i][j+1] and now == board[i+1][j] and now == board[i+1][j+1]:
                    rm.add((i,j))
                    rm.add((i+1,j))
                    rm.add((i,j+1))
                    rm.add((i+1,j+1))
                
        if rm:
            answer += len(rm)
            for i,j in rm:
                board[i][j] = []
            rm = set()
        else:
            break
            
        while True:
            move = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        move=1
            
            if move == 0:
                break
    
    

    #print(answer)
    #print(board)
    return answer
solution(4,5,["CCBDE", 
              "AAADE", 
              "AAABF", 
              "CCBBF"])
