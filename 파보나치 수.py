def solution(n):
    
    f_list = [0 for i in range(100001)]
    #print(f_list)
    f_list[0] = 0
    f_list[1] = 1
    
    start = 2
    while start<=n:
        f_list[start] = f_list[start-1] + f_list[start-2]
        start += 1

    answer = f_list[n]%1234567
    print(answer)
    return answer
solution(3)