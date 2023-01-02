def solution(quiz):
    #quiz = quiz.split('+')
    answer = []
    for i in quiz:
        i = i.replace(' ','')
        if eval(i.split('=')[0]) == int(i.split('=')[-1]):
            answer.append('O')
        else:
            answer.append('X')
    print(answer)
    return answer
solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])