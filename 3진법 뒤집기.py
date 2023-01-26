#3진수 변환 함수
def Trinary_digit(n):
    Trinary_digit_list =[]
    while True:
        a = divmod(n,3)
        Trinary_digit_list.insert(0,a[1])
        if a[0] == 0:
            break
        else:
            n=a[0]
    return int(''.join(map(str,Trinary_digit_list)))

def solution(n):
    answer = 0
    number = 0
    
    #앞뒤 반전
    reverse = str(Trinary_digit(n))[::-1]
    print(reverse)

    #10진법으로 표현하기
    for i in range(-1,-(len(reverse)+1),-1):
        answer += (3**number)*int(reverse[i])
        number += 1
    
    return answer
solution(45)



