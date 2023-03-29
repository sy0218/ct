#최소공배수 구하기 최소공배수 = (a*b)//최대공약수
def least(a,b):
    A,B=a,b
    #최대공약수 구하기
    while b != 0:
        a,b = b,a%b
    GCD = a
    return (A*B)//GCD
#print(least(2,7))

def solution(arr):
    answer = 0
    term = arr[0]
    for i in range(1,len(arr)):
        term = least(term, arr[i])
    print(term)
    answer = term
    return answer
solution([2,6,8,14])

