#수정 포인트
#len이 더큰 리스트를 기준으로
#len이 작은 리스트 for문돌리면서 큰리스트에 값이
#있으며 continue 없으면 append
#최종적으로 삽입된 리스트에서 교집합을 나눈 값이
#자카드 유사도 이다
'''
def solution(str1, str2):
    answer = 0
    #소문자로 통일
    str1 = str1.lower()
    str2 = str2.lower()

    #2개씩 끊은 문자열 리스트 만들기
    str1_list = []
    str2_list = []
    for i in range(len(str1)-1):
        #알파벳으로 이루어지지 않으면 삽입 x
        if str1[i:i+2][0].isalpha() and str1[i:i+2][1].isalpha():
            str1_list.append(str1[i:i+2])
             
    for i in range(len(str2)-1):
        #알파벳으로 이루어지지 않으면 삽입 x
        if str2[i:i+2][0].isalpha() and str2[i:i+2][1].isalpha():
            str2_list.append(str2[i:i+2])
    
    same=0
    if len(str1_list) > len(str2_list):
        max_list=str1_list
        low_list=str2_list
    else:
        max_list=str2_list
        low_list=str1_list
    
    for i in low_list:
        if i in max_list:
            same+=1
        else:
            max_list.append(i)

    if len(max_list)==0 and len(low_list)==0:
        return 65536
    
    #자카드 유사도 구하기(교집합 수/합집합 수)
    jaka=same/len(max_list)
    #최종적으로 jaka에 65536곱해주고 int만 출력
    answer = int(jaka*65536)
    #print(str1_list)
    #print(str2_list)
    
    #print(jaka)
    #print(answer)
    return answer
solution('E=M*C^2', 'e=m*c^2')
'''
'''
from collections import Counter

a=['aa','aa','aa']
b=['aa','aa']
a=Counter(a)
b=Counter(b)

print((a|b))
'''
from collections import Counter
def solution(str1,str2):
    answer = 0
    #소문자로 통일
    str1 = str1.lower()
    str2 = str2.lower()
    
    #2개씩 끊은 리스트
    str1_list=[]
    str2_list=[]

    for i in range(len(str1)-1):
        if str1[i:i+2][0].isalpha() and str1[i:i+2][1].isalpha():
            str1_list.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2][0].isalpha() and str2[i:i+2][1].isalpha():
            str2_list.append(str2[i:i+2])
    
    #자카트 유사도 구하기
    str1_list = Counter(str1_list)
    str2_list = Counter(str2_list)

    #교집합
    union=list((str1_list&str2_list).elements())
    #print(union)
    #합집합
    sum = list((str1_list|str2_list).elements())
    #print(sum)

    #쌍이없으면 66536리턴 
    if len(union)==0 and len(sum)==0:
        answer = 65536
    #자카트유사도계산수int로 소숫점제거
    else:
        answer = int((len(union)/len(sum))*65536)
    #print(answer)
    return answer
solution('FRANCE','french')