import datetime

today = datetime.date.today()
y = today.year

def solution(age):
    answer = 0
    answer = (y-age)+1
    print(answer)
    return answer

solution(40)