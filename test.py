def solution(d, budget):
    answer = 0
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
solution([2,2,3,3],10)

#먼저 정렬을 한후
#whlie 반복문
#예산의 합이 budget보다 같아지거나 작아질때까지 pop해주기
#반복문 종료되면 배열d의 길이를 리턴하여 지원할수 있는 부서 숫자 출력

