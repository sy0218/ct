def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        s=i//n
        r=i%n
        max_num = max(s,r)
        answer.append(max_num+1)
    print(answer)
    return answer
solution(4,7,14)

#1.n*n배열 만들기
#빈칸에 숫자를 채움
'''
def solution(n, left, right):
    answer = []
    n_array = []

    #배열만듬
    for i in range(1,n+1):
        list=[]
        for j in range(1,n+1):
            list.append(max(i,j))
        n_array.append(list)
    
    #배열의 행을 잘라 1차원 배열로 만듬
    for i in n_array:
        for j in i:
            answer.append(j)
    
    answer = answer[left:right+1]
    print(answer)
    #print(n_array)
    return answer
solution(4,7,14)
'''
