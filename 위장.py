def solution(clothes):
    answer = 1
    dict = {}
    for i in clothes:
        if i[-1] not in dict:
            dict[i[-1]] = [i[0]]
        else:
            dict[i[-1]].append(i[0])
    #각 의상종류 경우의 수에 안입는 경우도 있으니
    #+1을하여 다곱하고 마지막에 아무것도
    #안입는경우를 뺴준다
    #print(dict)
    for i in dict:
        answer *= len(dict[i])+1
    print(answer)
    answer-1
    return answer
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
