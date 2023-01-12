def solution(lines):
    answer = 0
    for i in range(3):
        l1, l2 = lines[i-1],lines[i]
        l1s, l2s = l1[0], l2[0]
        l1e, l2e = l1[1], l2[1]
        start_max = max(l1s, l2s)
        end_min = min(l1e, l2e)
        if start_max < end_min:
            answer += end_min-start_max
    

    l1, l2, l3 = lines[0], lines[1], lines[2]
    l1s, l2s, l3s = l1[0], l2[0], l3[0]
    l1e, l2e, l3e = l1[1], l2[1], l3[1]
    start_max = max(l1s, l2s, l3s)
    end_min = min(l1e, l2e, l3e)
    if start_max < end_min:
        answer -= (end_min - start_max)*2
    print(answer) 
    return answer
solution([[0, 5], [3, 9], [1, 10]])
#겹치는 선 찾기
#1. i[0] > j[0] 일떄 j[1] > i[0] 야됨 그럼 j[1]-i[0]
#단. i[1]보다 커지면 i[1]-i[0]

#2. i[0] < j[0] 일떄 i[1] > j[0] 야됨 그러면 i[1] - j[0]
#단 i[1] > j[1] 이면 j[1] - j[0]

