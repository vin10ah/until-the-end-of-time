def solution(clothes):
    c_dic = {}            
    for item, category in clothes:
        if category in c_dic:
            c_dic[category] += 1
        else:
            c_dic[category] = 1
            
    count = 1    
    for i in c_dic.values():
        count *= i+1

        
    return count-1