def solution(id_list, report, k):
    answer = []
    singo_count_dic = {} #신고 당한 횟수
    singo_report_dic = {} #신고자가 신고한 명단
    stop_ps = [] #정지당한 인원

    #report리스트 중복을 먼저 제거해줌 중복신고는 1회로 해야되서
    report = list(set(report))
   
    for i in id_list:
        singo_count_dic[i]=0
        singo_report_dic[i]=[]
    
    for i in report:
        singo_count_dic[i.split(' ')[-1]] += 1
        singo_report_dic[i.split(' ')[0]].append(i.split(' ')[-1])
        
    #print(singo_count_dic)
    #print(singo_report_dic)
    
    for i in singo_count_dic:
        #print(singo_count_dic[i])
        if singo_count_dic[i]>=k:
            stop_ps.append(i)

    #print(stop_ps)
    for i in singo_report_dic:
        a=0
        for j in stop_ps:
            if j in singo_report_dic[i]:
                a+=1
        answer.append(a)
    print(answer)
    return answer
solution(["con", "ryan"],
         ["ryan con", "ryan con", "ryan con", "ryan con"],
         3)