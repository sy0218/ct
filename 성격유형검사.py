
def soluiton(survey, choices):
    answer = ''
    score_dic = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    #score_dic['AN'] = score_dic['AN']+2
    #print(score_dic['AN'])
    
    
    for i in range(len(choices)):
        if choices[i]-4 > 0:
            select = survey[i][1]
            new = list(survey[i])
            new.sort()
            new = ''.join(new)
            if select=='T' or select=='F' or select=='M' or select=='N':
                score_dic[new] += -abs(choices[i]-4)

            else:
                score_dic[new] += abs(choices[i]-4)

        
        elif choices[i]-4 < 0:
            select = survey[i][0]
            new = list(survey[i])
            new.sort()
            new = ''.join(new)
            if select=='T' or select=='F' or select=='M' or select=='N':
                score_dic[new] += -abs(choices[i]-4)

            else:
                score_dic[new] += abs(choices[i]-4)

        elif choices[i]-4 == 0:
            continue


    for i in score_dic:
        if score_dic[i] >= 0:
            answer += i[0]
        elif score_dic[i] < 0:
            answer += i[1]
        
    print(answer)
    return answer
    
soluiton(["TR", "RT", "TR"],[7,1,3])

'''
a= ['am','cd','gt','ma']
new = list(a[3])
new.sort()
new = ''.join(new)
print(new)
'''