def solution(s):
    answer = True
    s = list(s.upper())
    p = s.count('P')
    y = s.count('Y')    
    return p == y