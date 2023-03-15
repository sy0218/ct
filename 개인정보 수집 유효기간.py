#날짜를 일로 바꾸는 코드
def total_day(date):
    year, month, day = map(int, date.split('.'))
    return (year*12*28)+(month*28)+day

def solution(today, terms, privacies):
    today_day = total_day(today)
    answer = []
    dic_terms = {}
    count = 1
    for i in terms:
        dic_terms[i[0]] = int(i.split(' ')[-1])
    
    for i in privacies:
        i_split = i.split(' ')
        privacies_date = i_split[0]
        term_date = dic_terms[i_split[-1]]

        privacies_day = total_day(privacies_date)+(term_date*28)-1
        print(today_day)
        print(privacies_day)
        if today_day > privacies_day:
            answer.append(count)
        
        count += 1
    
    print(answer)
    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"],
         ["2021.05.02 A",
          "2021.07.01 B",
          "2022.02.19 C",
          "2022.02.20 C"] )
'''
a='2022.5.9'
b='2022.5.9'
if a>b:
    print('o')
else:
    print('x')
'''