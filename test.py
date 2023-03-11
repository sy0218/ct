def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1,2,3,1]:
            del burger[-4:]
            answer+=1
    print(answer)
    return answer
solution([2, 1, 1, 2, 3, 1, 2, 3, 1])