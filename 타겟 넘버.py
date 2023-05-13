def dfs(numbers,target, curr_sum, curr_idx):
    if curr_idx == len(numbers):
        if curr_sum == target:
            return 1
        else:
            return 0
    else:
        answer = 0
        answer += dfs(numbers, target, curr_sum+numbers[curr_idx], curr_idx+1)
        answer += dfs(numbers, target, curr_sum-numbers[curr_idx], curr_idx+1)
    return answer

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    print(answer)
    return answer
solution([1,1,1,1,1], 3)