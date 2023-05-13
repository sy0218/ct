def solution(msg):
    answer = []
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #사전 딕셔너리 만듬
    alp_dic = {}
    num=1
    for i in alp:
        alp_dic[i] = num
        num+=1
    print(alp_dic)

    #msg가 없을떄까지 그냥 ㅈㄴㅈㄴㅈㄴㅈㄴㅈㄴ돌려
    while msg:
        for i in range(len(msg),0,-1):
            if msg[:i] in alp_dic:
                answer.append(alp_dic[msg[:i]])

                if msg[:i+1] not in alp_dic:
                    alp_dic[msg[:i+1]] = num
                    num+=1
                msg = msg[i:]
                break
        
    print(answer)
    return answer
solution('ABABABABABABABAB')




'''
a='1234'
list = {'1':1, '2':2, '3':3, '4':4}
num = 5
answer =[]
while True:
    for i in range(len(a),0,-1):
        if a[:i] in list:
            answer.append(list[a[:i]])
            list[a[:i+1]] = num
            num+=1
            a=a[i:]
    if len(a) == 0:
        break
print(answer)
print(list)
print(a)
'''