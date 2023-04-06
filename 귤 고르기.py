def solution(k, tangerine):
    answer = 0
    dict = {}
    
    #귤 종류마다 갯수를 카운트한 딕셔러니 만듬
    for i in list(set(tangerine)):
        dict[i] = 0
    for i in tangerine:
        dict[i] += 1

    #딕셔너리 귤 개수로 오름차순 정렬
    dict = sorted(dict.items(),
                  key=lambda x:x[1],
                  reverse=True)
    #print(dict)    

    for i in dict:
        k-=i[1]
        answer+=1
        if k<=0:
            break
    
    print(answer)
    return answer
solution(6, [1, 3, 2, 5, 4, 5, 2, 3])

