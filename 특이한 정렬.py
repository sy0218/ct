def solution(numlist,n):
    answer = []
    answer = sorted(numlist, key = lambda x:(abs(x-n),-x))
    #lambda를 사용하여 정렬
    print(answer)
    return answer
solution([1,2,3,4,5,6],4)