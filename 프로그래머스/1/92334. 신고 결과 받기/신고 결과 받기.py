# def solution(id_list, report, k):
#     r_dic = {}
#     answer = [0] * len(id_list)
    
#     for case in report:
#         user, block = case.split()
#         if block not in r_dic:
#             r_dic[block] = [user]
#         else:
#             r_dic[block].append(user)
            
#     for b_user, users in r_dic.items():
#         r_dic[b_user] = list(set(users))
    
#     for i in range(len(id_list)):
#         user = id_list[i]
#         count = r_dic[user]

#         if len(count) < k:
#             pass
#         else:
#             answer[i] += len(count)
        
            
#     return answer

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}
    
    for r in set(report):
        reports[r.split()[1]] += 1
        
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer
