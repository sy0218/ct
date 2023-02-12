def solution(n,arr1,arr2):
    answer = []
    graph1 = []
    graph2 = []
    for i in arr1:
        binary_list=[]

        while True:
            a=i//2
            b=i%2
            binary_list.append(b)
            
            if a == 0:
                break
            else:
                i=a

        if len(binary_list)<n:
            for i in range(n-len(binary_list)):
                binary_list.append(0)

        binary_list.reverse()
        graph1.append(binary_list)

    for i in arr2:
        binary_list=[]

        while True:
            a=i//2
            b=i%2
            binary_list.append(b)
            if a == 0:
                break
            else:
                i=a

        if len(binary_list)<n:
            for i in range(n-len(binary_list)):
                binary_list.append(0)

        binary_list.reverse()
        graph2.append(binary_list)

    for i in range(n):
        str = ''
        for j in range(n):
            if graph1[i][j]==1 or graph2[i][j]==1:
                str+='#'
            else:
                str+=' '
        answer.append(str)
    print(answer)

    return answer
solution(5,[9,20,28,18,11],[30,1,21,17,28])

