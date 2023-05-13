def div(num,n):
    answer = []
    dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6',
                7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C',
                13:'D', 14:'E', 15:'F'}
    while True:
        namogi = num % n
        answer.append(dict[namogi])
        num = num//n
        if num == 0:
            break
    answer = ''.join(answer[::-1])
    #print(answer)
    return answer
div(10,16)

def solution(n ,t, m, p):
    answer = ''
    num = 0
    talk_list = ''
    while True:
        talk_list += div(num,n)
        num += 1
        if len(talk_list) >= t*m:
            break
    

    while True:
        answer+=talk_list[p-1]
        p += m
        if len(answer) == t:
            break

    #print(talk_list)
    print(answer)
    return answer
solution(2,4,2,1)
