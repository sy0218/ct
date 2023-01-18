def solution(seoul):
    answer = ''
    seoul_index = seoul.index('Kim')
    answer = f'김서방은 {seoul_index}에 있다'
    print(answer)
    return answer
solution(["Jane", "Kim"])