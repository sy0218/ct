def solution(brown, yellow):
    answer=[]
    for i in range(1,int(yellow**(1/2))+1):
        if yellow%i == 0 and 2*(i+(yellow//i))+4==brown:
            answer = [(yellow//i)+2, i+2]
    print(answer)
    return answer
solution(24,24)