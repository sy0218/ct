def solution(dirs):
    answer = 0
    x,y = 0,0
    move_dict = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    move_path_list = []
    for i in dirs:
        if abs(x+move_dict[i][0])>5 or abs(y+move_dict[i][1])>5:
            continue

        move_x, move_y = x+move_dict[i][0], y+move_dict[i][1]
        move_path = [[x,y],[move_x,move_y]]
        move_path.sort()

        if move_path not in move_path_list:
            answer+=1
            move_path_list.append(move_path)
        
        x,y = move_x, move_y
    
    print(answer)
    return answer
solution("ULURRDLLU")