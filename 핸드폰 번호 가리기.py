def solution(phone_number):
    answer = ''
    answer = phone_number.replace(phone_number[0:-4],len(phone_number[0:-4])*'*')
    print(answer)
    return answer
solution("01033334444")
