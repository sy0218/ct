# set() 은 파이썬에서 집합을 의미
#유니크한 값을 가진다(중복x)

def solution(elemetns):
    answer = 0
    ele_list = set()
    elelen = len(elemetns)
    elemetns = elemetns*2

    num=1
    while num < elelen:
    
        for i in range(elelen):
            #print(elemetns[i:i+num])
            ele_list.add(sum(elemetns[i:i+num]))
        num+=1
    ele_list.add(sum(elemetns[:elelen]))
    #print(ele_list)
    answer = len(ele_list)
    #print(answer)
    return answer
solution([7,9,1,1,4])