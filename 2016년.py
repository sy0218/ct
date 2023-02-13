week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

def solution(a,b):
    answer = ''
    month_sum = 0
    for i in range(a-1):
        month_sum += months[i]
    month_sum += b
    answer = week[(month_sum%7)-1]
    print(answer)
    return answer
solution(5,24)