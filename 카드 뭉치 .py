def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in goal:
        if len(cards1) > 0 and cards1[0] == i:
            del cards1[0]
        elif len(cards2) > 0 and cards2[0] == i:
            del cards2[0]
        else:
            answer = 'No'
    print(answer)
    return answer
solution(["i", "water", "drink"],["want", "to"],
         ["i", "want", "to", "drink", "water"])