#sort와 sorted의 차이점은
#sorted는 새로운 리스트를 만들어줌 기존 리스트에 영향을 안줌
def solution(emergency):
    answer = []
    new_list = sorted(emergency,reverse=True)
    for i in emergency:
        answer.append(new_list.index(i)+1)
    return answer

print(solution([3,76,24]))