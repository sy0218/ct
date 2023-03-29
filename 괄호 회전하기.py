#1. 문자열 왼쪽으로 한칸씩 돌려보자
#2. 올바른 괄호이면 count해줌

def solution(s):
    answer = 0
    first_s = s
    while True:
        #올바른 괄호인지
        new_s = ''
        for i in s:
            new_s+=i
            if new_s[-2:] == '[]' or new_s[-2:] == '()' or new_s[-2:] == '{}':
                new_s = new_s[0:-2]
        
        #print(new_s)
        if len(new_s)==0 or new_s=='[]' or new_s=='()' or new_s=='{}':
            answer+=1
    
        #왼쪽으로 한칸씩 돌리기
        s=s[1:]+s[0]
        
        #처음과 같아지면 브레이크
        if s==first_s:
            break
        

    print(answer)
    return answer
solution("[](){}")
'''

#a="[](){}"
#a=a[1:]+a[0]
#print(a)
'''



'''

s="()[{}]"
new_s=''
for i in s:
    new_s+=i
    #print(new_a)
    if new_s[-2:] == '[]' or new_s[-2:] == '()' or new_s[-2:] == '{}':
        new_s = new_s[0:-2]

if len(new_s)==0 or new_s=='[]' or new_s=='()' or new_s=='{}':
    print(1)
    
'''