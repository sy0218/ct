def day_count(date):
    year, month, day = map(int, date.split('.'))
    return (year*12)*28 + month*28 + day

def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    count = 1
    for i in terms:
        term_dic[i.split(' ')[0]] = int(i.split(' ')[-1])
    #print(term_dic)

    for i in privacies:
        privacies_day = i.split(' ')[0]
        privacies_month = i.split(' ')[1]
        
        if day_count(today) > day_count(privacies_day) + (term_dic[privacies_month]*28)-1:
            answer.append(count)
        count+=1
    print(answer)


    return answer
solution("2022.05.19", ["A 6", "B 12", "C 3"],
         ["2021.05.02 A", 
          "2021.07.01 B", 
          "2022.02.19 C", 
          "2022.02.20 C"])
