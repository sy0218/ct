
def solution(people, limit):
    answer = 0
    people.sort()
    print(people)
    

    
    while len(people)>1:
        
        
        
        if people[0]+people[-1] <= limit:
            del people[0]
        people.pop()
        answer+=1
        

    if len(people)==1:
        answer+=1

    print(answer)
    return answer
solution([50, 70, 50, 80, 50],100)
'''

from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    dq = deque(people)
    print(dq)
    while len(dq) > 1:
        if dq[0] + dq[-1] <= limit:
            dq.popleft()
        answer += 1    
        dq.pop()
    if dq:
        answer+= 1
    print(answer)
    return answer

solution([50, 70, 50, 80, 50],100)


'''