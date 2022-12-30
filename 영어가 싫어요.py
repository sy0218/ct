def solution(numbers):
    answer = 0
    numbers_list ={"zero":"0", "one":"1", "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    for i in numbers_list.keys():
        if i in numbers:
            numbers = numbers.replace(i,numbers_list[i])
    answer = int(numbers)
    print(answer)
    return answer
solution("onetwothreefourfivesixseveneightnine")
#1.문자열 찾기 
#2. 넘버 리스트에 있는 문자 해당 숫자로 변경
#3.문자열 숫자로 변경