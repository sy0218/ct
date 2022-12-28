def solution(age):
    answer = ''
    string=['a','b','c','d','e','f','g','h','i','j']
    for i in str(age):
        answer += string[int(i)]
    return answer

print(solution(23))