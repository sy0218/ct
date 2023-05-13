from itertools import product
def solution(word):
    answer = 0
    word_dict_list = []
    for i in range(1,6):
        for j in product(['A','E','I','O','U'], repeat=i):
            word_dict_list.append(''.join(j))
    #print(word_dict_list)
    word_dict_list.sort()
    answer = word_dict_list.index(word)+1
    #print(answer)
    return answer
solution("AAAAE")
