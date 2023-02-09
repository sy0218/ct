def solution(sizes):
    answer = 0
    row_length = 0
    col_length = 0
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]

        if sizes[i][0]>row_length:
            row_length = sizes[i][0] 
        if sizes[i][1]>col_length:
            col_length = sizes[i][1]

    answer = row_length*col_length
    print(answer)
    return answer

solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])