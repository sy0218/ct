def solution(A,B):
    answer = 0
    text = list(A)
    for i in range(len(A)):
        if "".join(text) == B:
            return answer
        else:
            text.insert(0, text.pop())#마지막 문자를 리스트 가장 앞으로 옴
            answer += 1
            print(text)
    return -1
print(solution('apple', 'elppa'))