
def solution(new_id):
    answer = ''
    #1단계 대문자를 소문자로 치환
    for i in new_id:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i
    #print(answer)

    #2단계 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)
    #제외한 문자 모두 제외
    for i in answer:
        if i.islower() or i.isdigit() or i=='-' or i=='_' or i=='.':
            continue
        else:
            answer = answer.replace(i,'')
    #print(answer)

    #3단계 .가 두번 이상이면 연속된 부분을 하나의 마침표로 치환
    new_answer = answer[0]
    
    for i in range(1, len(answer)): 
        if answer[i] == '.' and new_answer[-1] ==  answer[i]:
            continue
        else:
            new_answer += answer[i]
    answer = new_answer
    #print(answer)

    #4단계 .가 처음이나 끝에 있다면 제거
    if answer[0] == '.' and len(answer)>1:
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]
    #print(answer)

    #5단계 빈문자열 이면 a를 대입
    if answer == '':
        answer = 'a'
    #print(answer)

    #6단계 길이가 16이상이면 15개만 남기고 제외
    #제외후 .가 끝에 위치한다면 문자제거
    if len(answer) >= 16:
        answer_list = list(answer)[0:15]

        if answer_list[-1] == '.':
            del answer_list[-1]

        answer = ''.join(answer_list)
    #print(answer)

    #7단계 길이가 2자이하면 마지막 문자를 길이가3이 될떄까지
    #반복해서 끝에 붙임
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    print(answer)
    return answer
solution("abcdefghijklmn.p")



    
        
