def asu(n):
    answer = 0
    list =[]
    for i in range(1, int((n**(1/2)))+1):
        if n%i == 0:
            if (n//i)**2 ==n:
                list.append(i)
            else:
                list.append(i)
                list.append(n//i)
    answer = len(list)
    #print(answer)
    return answer


def solution(n, k):
    answer = 0
    sosu = []

    while True:
        b = n%k
        n = n//k
        
        sosu.append(str(b))
        if n == 0:
            break
    
    sosu = ''.join(sosu[::-1])
    print(sosu)

    list = []
    point = -1
    for i in range(len(sosu)):
        if sosu[i] == '0':
            list.append(sosu[point+1:i])
            point = i
    list.append(sosu[point+1:])
    #print(list)
    
    for i in list:
        
        if len(i) == 0:
            continue
        
        if asu(int(i)) == 2:
            answer+=1
    #print(answer)
    
    return answer
solution(110011,10)
