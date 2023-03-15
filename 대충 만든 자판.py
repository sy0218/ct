def solution(keymap, targets):
    answer = []
    for i in targets:
        #클릭 카운트
        ck_count = 0
        for j in i:
            #최소 클릭 수를 구하기위해 리스트 변수 생성
            keymap_index =[]
            for k in keymap:
                if j in k:
                    keymap_index.append(k.index(j)+1)
                elif j not in k:
                    continue
            #만약 키맵인덱스가 0이면 만들수 없는 것이므로 
            #즉시 반복문을 멈추고 ck_count를 -1로 치환함   
            if len(keymap_index) == 0:
                ck_count = -1
                break
            #키맵 인덱스가 0이 아니면 만들수 있는 것이므로
            #키맵 인덱스 최솟값을 ck_count에 더해줌 
            else:
                ck_count += min(keymap_index)
        #최종적으로 클릭 카운트를 삽입 시켜줌
        answer.append(ck_count)

    print(answer)
    return answer
solution(["AGZ", "BSSS"],["ASA","BGZ"])