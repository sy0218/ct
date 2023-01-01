def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] == i[1]:
            answer = 'login'
        elif id_pw[0] == i[0] and id_pw[1] != i[1]:
            answer = 'wrong pw'
        elif id_pw[0] != i[0] and id_pw[1] != i[1]:
            answer = 'fail'
    print(answer)
    return answer
solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]])