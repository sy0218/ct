import statistics
def solution(score):
    answer = []
    avg_list = []
    for i in score:
        avg_list.append((statistics.mean(i)))
    
    for i in avg_list:
        answer.append(sorted(avg_list,reverse=True).index(i)+1)
    print(answer)
    return answer
solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])