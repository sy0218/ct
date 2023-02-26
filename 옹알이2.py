def solution(babbling):
    answer = 0
    talk_list = ['aya', 'ye', 'woo', 'ma']

    for i in talk_list:
        for j in range(len(babbling)):
            if i in babbling[j]:
                if i*2 in babbling[j]:
                    continue
                elif i in babbling[j]:
                    babbling[j] = babbling[j].replace(i,' ')
    #print(babbling)

    for i in babbling:
        
        if i.strip() == '':
            answer += 1
    print(answer)
    return answer

solution(["ayaye", "uuu", "yemayema", "yemawoo", "ayaayaa"])