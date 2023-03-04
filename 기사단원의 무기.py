#약수 구하기 효율적인 시간복잡도 
def divisor(n):
    #약수를 담을 리스트
    divisor = []
    #1부터 제곱근까지만 반복문
    for i in range(1,int(n**(1/2)+1)):
        #나누어 떨어지면 약수 리스트에 추가
        if n%i == 0:
            divisor.append(i)
            #2*2=4 5*5=25 와같은 중복을 없애주기위해
            if i**2 != n:
                divisor.append(n//i)
    return divisor
#print(divisor(6))


def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        #리미트를 초과 안할시 그냥 더해줌
        if len(divisor(i)) <= limit:
            answer+=len(divisor(i))
        #리미트를 초과시 power로 더해줌
        elif len(divisor(i)) > limit:
            answer += power
    #print(answer)
    return answer
solution(5,3,2)