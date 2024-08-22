def solution(N, stages):
    dic = {}
    fail = {(i+1):0 for i in range(N)}
    stages.sort()
    
    for stage in stages:
        if stage not in dic:
            dic[stage] = 1
        # elif stage == N+1:
        #     continue
        else:
            dic[stage] += 1
    print(fail)
    
    s_cnt = len(stages)
    
    for stage in range(1, N+1):
        if stage in dic:
            if s_cnt != 0:
                fail[stage] = dic[stage] / s_cnt
                s_cnt -= dic[stage]
            else:
                fail[stage] = 0
    
    sorted_dict = dict(sorted(fail.items(), key = lambda item: item[1], reverse = True))
    
    return list(sorted_dict.keys())


