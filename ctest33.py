def solution(s1, s2):
    answer = 0
    for i1 in s1:
        for i2 in s2:
            if i1==i2:
                answer = answer+1
            else:
                continue
    print(answer) 
    return answer

solution(['a','b','c'],['com','b','d','p','c'])