def solution(s):
    answer = 0
    
    while True:
        if len(s) == 0:
            break
        x = s[0]
        x_count = 0
        other_count = 0

        for i in range(len(s)):
            if i == len(s)-1:
                s=''
                break

            if s[i] == x:
                x_count += 1
                if x_count == other_count:
                    s=s[i+1:]
                    break 
            elif s[i] != x:
                other_count += 1
                if other_count == x_count:
                    s=s[i+1:]
                    break
        answer += 1
    print(answer)
    return answer
solution("abracadabra")