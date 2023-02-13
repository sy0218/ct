def solution(nums):
    answer = 0
    new_nums = []
    for i in nums:
        if i not in new_nums:
            new_nums.append(i)
    answer = min(len(new_nums), len(nums)//2)
    
    return answer
print(solution([3,1,2,3]))