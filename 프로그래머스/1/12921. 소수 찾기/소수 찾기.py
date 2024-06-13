# def solution(n):
#     num_list = list(range(2, n+1))
#     answer = 0
#     prime = []
    
#     for num in num_list:
#         check=True
#         for p in prime:
#             if num%p==0:
#                 check = False
#                 break
#         if check:
#             prime.append(num)
#     return len(prime)

def solution(n):
    pset = set(range(2, n+1))
    
    for num in range(2, n+1):
        pset -= set(range(num*2, n+1, num))
        
    return len(pset)
    
    
    
    
    
    