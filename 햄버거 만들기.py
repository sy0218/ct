def solution(ingredient):
    answer=0
    list_ingredient = []
    for i in ingredient:
        list_ingredient.append(i)
        if list_ingredient[-4:] == [1,2,3,1]:
            del list_ingredient[-4:]
            answer+=1
    print(answer)
    return answer
solution([2, 1, 1, 2, 3, 1, 2, 3, 1])


