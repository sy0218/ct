def solution(cachesize, cities):
    answer = 0
    cash_list = []
    if cachesize==0:
        answer = 5*len(cities)

    else:
        for i in cities:
            i = i.upper()
            
            if i in cash_list:
                cash_list.remove(i)
                cash_list.append(i)
                answer+=1
            else:
                if len(cash_list)<cachesize:
                    cash_list.append(i)
                    answer+=5
                else:
                    cash_list.pop(0)
                    cash_list.append(i)
                    answer+=5
        

    #print(answer)
    return answer
solution(0,
         ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])

'''
a=[1,2,3,4]
a.pop(0)
print(a)
'''