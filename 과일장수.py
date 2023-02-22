'''
a = [1,2,3,4,5,1,2,5]
del a[a.index(max(a))]
print(a)
'''
'''
def solution(k,m,score):
    answer = 0
    box = []
    if k<1 or len(score)<m:
        return 0
    else:
        while len(score) > 0:
            box.append(max(score))
            del score[score.index(max(score))]

            if len(box) == m:
                answer += min(box)*m
                box = []
    
    
    print(answer)
    return answer
    
solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
'''

def solution(k,m,score):
    answer = 0
    
    if k<1 or len(score)<m:
        return 0
    else:
        num = 0
        score.sort(reverse=True)
        while num+m <= len(score):
            answer += min(score[num:num+m])*m
            num = num+m     

    return answer
solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])