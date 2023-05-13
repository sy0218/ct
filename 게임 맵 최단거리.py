from collections import deque
def solution(maps):
    answer = 0
    queue = deque([(0,0)])
    move = [(0,1),(0,-1),(1,0),(-1,0)]

    while queue:
        x,y = queue.popleft()
        for i in move:
            xx = x+i[0]
            yy = y+i[1]
            if 0<=xx<len(maps) and 0<=yy<len(maps[0]) and maps[xx][yy]==1:
                maps[xx][yy] = maps[x][y]+1
                queue.append((xx,yy))
    #print(maps)
    if maps[-1][-1] > 1:
        answer = maps[-1][-1]
    else:
        answer = -1
    return answer
solution([[1,0,1,1,1],
          [1,0,1,0,1],
          [1,0,1,1,1],
          [1,1,1,0,1],
          [0,0,0,0,1]])