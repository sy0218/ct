def solution(num):
    list = []
    for i in range(1,int(num**(1/2)+1)):
        if num % i == 0:
            if i**2 == num:
                list.append(i)
            else:
                list.append(i)
                list.append(num//i)
    list.remove(1)
    return list                


def solution(arr):
    answer = 0
    
    while True:
        if len(arr)==1:
            break
        list = []
        for j in div(arr[0]):
            if j in div(arr[1]):
                list.append(j)
        
        if list:
            arr[1] = arr[0]*arr[1]//max(list)
        else:
            arr[1] = arr[0]*arr[1]
        
        arr.pop(0)
    print(arr)
    return answer
solution([2,6,8,14])