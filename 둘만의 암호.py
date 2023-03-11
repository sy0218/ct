
def solution(s,skip,index):
    answer = ''
    spk = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #skip에 있는 문자 삭제
    for i in skip:
        spk.remove(i)

    for i in s:
        answer += spk[(spk.index(i)+index)%len(spk)]

    print(answer)
    return answer
solution('aukks', 'wbqd', 5)