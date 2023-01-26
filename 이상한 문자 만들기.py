def solution(s):
    answer = ''
    for i in s.split(' '):
        for k in range(len(i)):
            if k%2==0:
                answer += i[k].upper()
            else:
                answer += i[k].lower()
        answer += ' ' #<<<< 여기서 마지막에 공백이 들어감
    print(answer)
    return answer[0:-1]#마지막에 공백이 들어가기 떄문에!!

solution("try hello world")