
def solution(a,b):
    answer = 0
    a.sort()
    b.sort(reverse=True)
    
    for i in range(len(a)):
        answer+=a[i]*b[i]
    print(answer)
    return answer
solution([1,2],[3,4])
'''
a=[1,2,3,4]
#a.sort(reverse = True)
#a.reverse()
print(a)
'''