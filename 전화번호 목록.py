def solution(phone_book):
    answer = True
    
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
    print(hash_map)
    for i in phone_book:
        str = ''
        for j in i:
            str+=j

            if str in hash_map and str != i:
                answer = False
    #print(answer)
    return answer
solution(["119", "97674223", "1195524421"])