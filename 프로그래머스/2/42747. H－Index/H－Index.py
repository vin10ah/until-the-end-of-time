def solution(citations):
    n = len(citations)
    answer = 0
    citations.sort()   
    for h in range(1, n+1):
        c_cnt = 0
        if n < h:
            continue
        else:  
            for c in citations:
                if c >= h:
                    c_cnt += 1
        if c_cnt >= h:
            answer = h
    
    return answer