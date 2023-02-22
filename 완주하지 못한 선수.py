def solution(participant, completion):
    answer = ''
    hash_dict = {}
    sumhash = 0

    #hash_dict에 해쉬값을 키로 값을 넣음
    for i in participant:
        hash_dict[hash(i)] = i
        #모든 해시값을 다 더함
        sumhash += hash(i)

    for i in completion:
        #completion에 있는 값에 대한 해시값을 다뺴줌
        sumhash -= hash(i)
    #결굴 남는 해시값이 완주하지 못한 1명
    answer = hash_dict[sumhash]
    print(answer)
    return answer
solution(["marina", "josipa", "nikola", "vinko", "filipa"]
, ["josipa", "filipa", "marina", "nikola"])