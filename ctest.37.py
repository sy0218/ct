def solution(hp):
    answer = 0
    if hp%5==0:
        answer = hp//5
    else:
        if (hp%5)%3==0:
            answer = hp//5+((hp%5)//3)
        else:
            answer = hp//5+((hp%5)//3)+(((hp%5)%3)//1)
    print(answer)

    return answer

solution(24)