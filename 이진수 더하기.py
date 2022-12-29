def solution(bin1,bin2):
    answer = ''
    #2진수를 10진수로 변환
    a = int('0b'+bin1,2)
    b = int('0b'+bin2,2)
    #10진수를 더함
    c = a+b
    #10진수를 2진수로 변한
    c = bin(c)
    #앞에0b삭제
    str(c).replace('0b','',1)
    answer = str(c).replace('0b','',1)
    print(answer)
solution('10','11')