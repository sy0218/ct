
def solution(n, words):
    answer = [0,0]

    spk_list = []
    for i in range(len(words)):
        
        if len(spk_list)>=1:
            if words[i] in spk_list or words[i][0] != spk_list[-1][-1]:
                print(i)
                answer[0] = (i%n)+1
                answer[1] = (i//n)+1
                break

        spk_list.append(words[i])
    print(answer)
    return answer
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
'''

a = ['asdf','fdsa']
print(a[-1][-1])
'''