def solution(record):
    answer = []
    name_dic={}
    for i in record:
        if ('Enter' in i) or ('Change' in i):
            name_dic[i.split(' ')[1]] = i.split(' ')[2]
    print(name_dic)
    
    for i in record:
        
        id = name_dic[i.split(' ')[1]]
        
        
        if 'Enter' in i:
            answer.append(f'{id}님이 들어왔습니다.')
        elif 'Leave' in i:
            answer.append(f'{id}님이 나갔습니다.')    
    
    print(answer)
    return answer
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])