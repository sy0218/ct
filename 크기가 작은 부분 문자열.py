def solution(t,p):
    answer = 0
    #print(t[0:len(p)])
    i=0
    while i+len(p)<=len(t):
        print(t[i:i+len(p)])
        if t[i:i+len(p)] <= p:
            answer+=1
            
        i+=1
    print(answer)
    return answer
solution("500220839878","7")