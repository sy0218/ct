def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    people = [a1,a2,a3]
    
    correct_list = []
    
    
    for i in people:
        correct=0
        for j in range(len(answers)):
            
            if answers[j] == i[j%len(i)]:
                correct+=1

        correct_list.append(correct)
    print(correct_list)
    
    for i in range(len(correct_list)):
        if correct_list[i] == max(correct_list):
            answer.append(i+1)
    print(answer)
    return answer
solution([1,3,2,4,2,4])