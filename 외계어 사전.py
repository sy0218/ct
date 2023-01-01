def solution(spell, dic):
    answer = 0
    new_dic =[]
    for i in dic:
        new_dic.append(''.join(sorted(i)))
    if ''.join(sorted(spell)) in new_dic:
        answer = 1
    else:
        answer = 2
    print(answer)
    return answer
solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"])