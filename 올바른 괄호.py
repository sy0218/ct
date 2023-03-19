
def solution(s):
    a=[]
    for i in s:
        a.append(i)
    
        if a[-2:]==['(',')']:
            a.pop()
            a.pop()
    #print(a)
    if len(a) == 0:
        return True
    else:
        return False
print(solution(")()("))
'''

a=[1,2,3,4]

print(a[-2:])
'''
