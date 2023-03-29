#최소 공배수 구하기 최소공배수 = (a*b)//최대공약수
def least(a,b):
    A,B=a,b
    #최대 공약수
    while b!=0:
        a,b = b,a%b

    gcd = a
    return (A*B)//gcd


def solution(arr):
    answer = 0
    arr.sort()    
    temp = least(arr[0],arr[1])

    for i in range(2,len(arr)):
        temp = least(temp,arr[i])
    #print(temp)
    answer = temp
    return answer
solution([2,6,8,14])

