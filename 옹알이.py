'''list = ["aya", "yee", "u", "maa", "wyeoo"]
answer = 0
for i in list:
    list[list.index(i)] = i.replace('aya','')

for i in list:
    if len(i) == 0:
        answer += 1
print(list)
print(answer)'''


def solution(babbling):
    answer = 0
    talk = ["aya", "ye", "woo", "ma"]
    for i in talk:
        for k in babbling:
            if i in k:
                babbling[babbling.index(k)] = k.replace(i,'*')
    
    print(babbling)
    for a in babbling:
        if len(a) == a.count('*'):
            answer += 1
    print(answer)
    return answer
solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])