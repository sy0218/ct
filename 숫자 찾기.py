def solution(num,k):
    answer = 0
    if str(k) in str(num):
        for i in list(str(num)):
            if i == str(k):
                answer = list(str(num)).index(i)+1
    else:
        answer = -1
    return answer

print(solution(232443,4))