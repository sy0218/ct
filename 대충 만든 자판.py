def solution(keymap, targets):
    answer = []
    for i in targets:
        ck_count = 0
        for j in i:
            keymap_index =[]
            for k in keymap:
                if j in k:
                    keymap_index.append(k.index(j)+1)
                elif j not in k:
                    continue
            if len(keymap_index) == 0:
                ck_count = -1
                break
            else:
                ck_count += min(keymap_index)
        answer.append(ck_count)

    print(answer)
    return answer
solution(["AGZ", "BSSS"],["ASA","BGZ"])