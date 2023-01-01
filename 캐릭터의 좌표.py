def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput:
        if i == 'up' and answer[1] < board[1]//2:
            answer[1] += 1
        elif i == 'down' and answer[1] > (-board[1])//2+1:
            answer[1] -= 1
        elif i == 'right' and answer[0] < board[0]//2:
            answer[0] += 1
        elif i == 'left' and answer[0] > (-board[0]//2)+1:
            answer[0] -= 1
    print(answer)
    return answer
solution(["down", "down", "down", "down", "down"],[7, 9])