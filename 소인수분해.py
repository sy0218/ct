def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n%i == 0:
            n=n/i
            answer.append(i)
        else:
            i +=1
    answer = sorted(list(set(answer)))
    print(answer)
    return answer
solution(420)

#1. 2부터 ++ 하면서 나눠서 나머지 0 되는거 찾기
#2. 나머지가 0이 아닐떄까지 반복
#3. 언제까지? 마지막 나눗기 했을떄 몫이 1이되면 그만