def solution(s, skip, index):
    answer=''
    alp = ['a','b','c','d','e','f','g','h','i','j','k',
           'l','m','n','o','p','q','r','s','t','u','v','w','x',
           'y','z']
    
    for i in skip:
        alp.remove(i)
    
    print(alp)
    for i in s:
        answer += alp[(alp.index(i)+index)%len(alp)]

    print(answer)
    return answer
solution("aukks", "wbqd", 5)