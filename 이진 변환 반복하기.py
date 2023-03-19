# 0을 제거후 자리수반큼 이진변환
#0 제거후 1이되면 break

def bin(num):
    binary = ''
    while True:
        #몫
        a = num//2
        #나머지
        b = num%2
        binary += str(b)

        num=a
        if num == 0:
            break
    return binary[::-1]
#print(bin(len("1")))


def solution(s):
    answer = []
    bin_count = 0
    remove_0_count = 0

    while s!='1':
        remove_0_count += s.count('0') #삭제할 0개수 확인
        s=s.replace('0','') #0을 없에기
        s = bin(len(s)) #길이 만큼 이진변환
        bin_count+=1
    
    answer = [bin_count,remove_0_count]
    print(answer)
    return answer
solution("01110")

