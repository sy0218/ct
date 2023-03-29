def solution(s):
    answer = 0
    new_list = []
    for i in s:
        new_list.append(i)
        if len(new_list)>=2 and new_list[-1]==new_list[-2]:
            del new_list[-2:]
    
    if len(new_list) == 0:
        answer = 1
    #print(answer)
    #print(new_list)        
    return answer
solution('baabaa')
'''

a='aafaaf'
a= a.replace('a','')
print(a)
'''