def solution(board):
    answer = 0
    
    for i in range(len(board)):
        if 1 in board[i]:
            #print(i)
            for a in range(len(board[i])):
                #print(board[i][a])
                if board[i][a] == 1:
                    #print(a)
                    
                    try:
                        for c in range(-1,2):
                            if board[i-1][a+c] != 1:
                                board[i-1][a+c]=2
                            else:
                                board[i-1][a+c] =1
                        #board[i-1][a-1]=2
                        #board[i-1][a]=2
                        #board[i-1][a+1]=2
                        for c in range(-1,2,2):
                            if board[i][a-1] != 1:
                                board[i][a-1] = 2
                            else:
                                board[i][a-1]=1
                        #board[i][a-1]=2
                        #board[i][a+1]=2
                        for c in range(-1,2):
                            if board[i+1][a+c] != 1:
                                board[i+1][a+c]=2
                            else:
                                board[i+1][a+c] =1
                        #board[i+1][a-1]=2
                        #board[i+1][a]=2
                        #board[i+1][a+1]=2
                    except IndexError:
                        continue
    print(board)
    for i in board:
        answer += i.count(0)

    print(answer)
    return answer

solution([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]])
#1. 죄뢰가 있는 줄 찾기
#2. 줄에서 죄뢰의 인덱스 찾기
