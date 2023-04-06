'''
def solution(s):
    answer = []
    #print(s)
    s=s.replace('{{','')
    s=s.replace('}}','')
    #print(s)
    s=s.split('},{')
    #print(s)
    #문자열 길이순으로 정렬
    s=sorted(s,key=len)
    #print(s)
    for i in s:
        if i.isdigit()==True:
            answer.append(int(i))
        else:
            i=i.split(',')
            for j in i:
                if int(j) not in answer:
                    answer.append(int(j))
    print(answer)
    return answer

solution("{{20,111},{111}}")
'''
'''
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')
    print(s1)
    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)
    print(new_s)
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
solution("{{20,111},{111}}")
'''


def solution(s):
    answer = []
    s=s.lstrip('{').rstrip('}').split('},{')

    new_list=[]
    for i in s:
        i=i.split(',')
        new_list.append(i)
    print(new_list)

    new_list.sort(key=len)

    for i in new_list:
        for j in i:
            if j not in answer:
                answer.append(j)
    answer = list(map(int,answer))
    print(answer)
    return answer

solution("{{20,111},{111}}")