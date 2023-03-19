#이진수 변환
def binary(num):
    bin_num = ''
    while True:
        b=num%2
        num = num//2
        bin_num+=str(b)
        if num == 0:
            break
    bin_num = bin_num[::-1]
    #print(bin_num)
    return bin_num



def solution(n):
    answer = 0
    one_count = binary(n).count('1')
    #print(one_count)

    while True:
        n+=1
        if one_count == binary(n).count('1'):
            break
    
    answer = n
    print(answer)
    return answer
solution(78)