#데크(deque)의 개념
#보통 큐(queue)는 선입선출(FIFO) 방식으로 작동한다. 
#반면, 양방향 큐가 있는데 그것이 바로 데크(deque)다.
from collections import deque#데크 사용

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1) # rotate() 함수를 이용해 오른쪽 1칸
    elif direction == 'left':
        numbers.rotate(-1) #rotate() 함수를 이용해 왼쪽으로 1칸
    
    return list(numbers)

print(solution([1,2,3],'right'))