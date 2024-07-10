def solution(str_list):
    
    for s in str_list:
        if s == 'l':
            idx = str_list.index(s)
            return str_list[:idx]
        elif s == 'r':
            idx = str_list.index(s)
            return str_list[idx+1:]
    
    return []
        
