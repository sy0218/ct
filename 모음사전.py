#완전탐색 중복 순열을 위한 product함수 임포트
from itertools import product
def solution(word):
    answer = 0
    #모든 단어의 경우의 수를 담을 리스트 선언
    word_dict_list = []
    #중복순열 1~5개 문자 
    for i in range(1,6):
        for j in product(['A','E','I','O','U'],repeat=i):
            #word_dict_list에 문자 삽입
            word_dict_list.append(''.join(j))
    #사전순으로 정렬을 위한 sort()
    word_dict_list.sort()
    #몇번쨰 숫자인지 확인을 위해 index + 1 을 해줌
    answer = word_dict_list.index(word)+1
    
    print(len(word_dict_list))
    print(answer)
    return answer
solution('AAAAE')

