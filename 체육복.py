def solution(n, lost, reserve):
    #차집합 연산을 위해 set사용

    lost_num = set(lost)-set(reserve)
    reserve_num = set(reserve) - set(lost)
    #print(lost_num)
    #print(reserve_num)
    answer = n-len(lost_num)
    
    for i in lost_num:
        for j in list(reserve_num):
            
            #여벌의 체육복을 받게 되면 answer을 증감시키고
            #여벌의 빌려준 체육복을 여벌 리스트에서 삭제후 반복문 종료
            if i-1 == j or i+1 ==j:
                answer += 1
                reserve_num.remove(j)
                break
    print(answer)
    return answer
solution(5,[2,4],[1,3,5])












'''a=[1,2,3,4,5]
#del a[0]
a.remove(3)
print(a)'''