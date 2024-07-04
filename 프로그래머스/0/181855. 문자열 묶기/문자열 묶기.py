def solution(strArr):
    len_s = {}
    for s in strArr:
        if len(s) in len_s:
            len_s[len(s)] += 1
        else:
            len_s[len(s)] = 1
        
    return max(len_s.values())