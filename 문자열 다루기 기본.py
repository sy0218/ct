def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit()==True:
        return True
    else:
        return False
print(solution("1234"))