def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer+=f'{i}'*(food[i]//2)
    answer += '0'
    
    list_answer = list(answer[0:len(answer)-1])
    list_answer.reverse()
    answer += ''.join(list_answer)
    print(answer)
    return answer
solution([1, 3, 4, 6])