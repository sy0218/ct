#결국은 10일 안에 want상품을 다구해할수 있으면
#된가는거잔음 수량까지 다

def solution(want, number, discount):
    answer = 0
    while True:
        dis_10 = discount[0:10]
        if len(dis_10) < 10:
            break
        
        count = 0
        for i in range(len(want)):
            if dis_10.count(want[i])>=number[i]:
                count+=1
        if count == len(want):
            answer+=1
        
        discount.pop(0)

    print(answer)
    return answer
solution(["banana", "apple", "rice", "pork", "pot"],
         [3, 2, 2, 2, 1],
         ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
'''

a=['a','b','c','d']
a.pop(0)
print(a)
'''
