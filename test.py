def solution(wallpaper):
    answer = []
    x=[]
    y=[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            #print(j)    
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
        #print(wallpaper[i])
    #print(x)
    #print(y)
    answer = [min(x),min(y),max(x)+1,max(y)+1]
    print(answer)
    return answer
solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])