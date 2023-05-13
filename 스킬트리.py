
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_str = ''
        for j in i:
            if j in skill:
                skill_str+=j
        #print(skill_str)
        #print(skill[0:len(skill_str)])
        if skill_str == skill[0:len(skill_str)]:
            answer+=1
    print(answer)

    return answer
solution('CBD',	["BACDE", "CBADF", "AECB", "BDA"])
'''
a='BCD'
print(a[0:len(a)-1])
'''