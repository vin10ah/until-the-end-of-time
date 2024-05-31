def solution(participant, completion):
    p_dic = {}
    for name in participant:
        if name in p_dic:
            p_dic[name] += 1
        else:
            p_dic[name] = 1
            
    for name in completion:
        p_dic[name] -= 1
    
    for n, s in p_dic.items():
        if s == 1:
            return n

# def solution(participant, completion):