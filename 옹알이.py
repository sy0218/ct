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