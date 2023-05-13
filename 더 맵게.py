#힙을 사용하는 이유 : 일반적인 리스트와 달리
#push() , pop() 이후 자동 정렬!!!
'''
import heapq

def solution(scoville,K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    print(heap)

    while heap[0] < K:
        if len(heap) <= 1:
            return -1
        else:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
            answer+=1
        
    print(answer)
    return answer
solution([1, 2, 3, 9, 10, 12],7)
'''
import heapq
def solution(scoville, k):
    answer = 0
    scoville.sort()

    while scoville[0] < k:
        if len(scoville) <= 1:
            return -1
        else:
            heapq.heappush(scoville, (heapq.heappop(scoville)+(heapq.heappop(scoville)*2)))
            answer+=1
    print(answer)
    return answer
solution([1,2,3,9,10,12], 7)