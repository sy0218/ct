def solution(s):
    answer = 0
    while True:
        if len(s) == 1:
            answer += 1
            break
        elif len(s) == 0:
            break

        count_x = 1
        count_other = 0
        x = s[0]

        for i in range(1,len(s)):
            if i == len(s):
                s = ''
                break
            
            if s[i] != x:
                count_other += 1
                if count_x == count_other:
                    s = s[i+1:]
                    break

            if s[i] == x:
                count_x += 1
                if count_x == count_other:
                    s = s[i+1:]
                    break

            
        answer += 1
        
    print(answer)
    return answer
solution("aaabbaccccabba")