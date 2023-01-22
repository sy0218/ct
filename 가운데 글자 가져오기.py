def solution(s):
    answer =''
    #print(int((len(s)/2)-1))
    if len(s)%2 != 0:
        answer = s[len(s)//2]
    else:
        answer = s[(len(s)//2)-1:(len(s)//2)+1]
    print(answer)
    return answer
solution("qwer")