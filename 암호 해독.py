def solution(cipher, code):
    answer = ''
    answer=cipher[code-1::code]
    print(answer)
    return answer

solution("dfjardstddetckdaccccdegk",4)