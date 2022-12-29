def solution(before, after):
    answer = 0
    after_list = list(after)
    for i in before:
        if i in after_list:
            after_list.remove(i)
        else:
            continue
    if len(after_list) == 0:
        answer = 1
    else:
        answer = 0
    return answer

print(solution('olleh','hello'))