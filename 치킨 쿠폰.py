'''1.쿠폰 1081개
2.1081개면 108개 서비스 치킨 쿠폰은 108개+1(남은 쿠폰)
3.쿠폰109개면 10마리 서비스 치킨 쿠폰은 10개+9
4.쿠폰 19개면 1마리 서비스 치킨 쿠폰은 1개+9
5.쿠폰 10개면 1마리 서비스 치킨 쿠폰은 1개'''

def solution(chicken):
    answer = 0
    cop = chicken
    while cop>=10:
        answer += cop//10
        cop = cop//10 + cop%10
    print(answer)
    return answer
solution(1081)