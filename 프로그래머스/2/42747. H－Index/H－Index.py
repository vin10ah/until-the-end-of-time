# def solution(citations):
#     n = len(citations)
#     answer = 0
#     lst = []
#     citations.sort()   
#     for h in range(1, n+1):
#         c_cnt = 0         
#         for c in citations:
#             if c >= h:
#                 c_cnt += 1
#         if c_cnt >= h:
#             answer = h
#             lst.append(h)
    
#     return lst

# def solution(citations):
#     n = len(citations)
#     citations.sort(reverse=True)
#     answer = 0
#     for h in citations:
#         c_cnt = 0       
#         for i in range(n):
#             if citations[i] >= h:
#                 c_cnt += 1
#         if c_cnt >= h:
#             return h
    #         answer = h
    # return answer
    
def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index
