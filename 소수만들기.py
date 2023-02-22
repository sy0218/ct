import math

#소수 판별 함수
def sosu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if sosu(nums[i]+nums[j]+nums[k])==True:
                    answer += 1
    print(answer)
    return answer
solution([1,2,3,4])

