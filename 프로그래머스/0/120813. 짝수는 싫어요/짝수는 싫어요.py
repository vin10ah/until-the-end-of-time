# def solution(n):
#     a = []
#     for i in range(n+1):
#         if i % 2 == 1:
#             a.append(i)
#     return a

def solution(n):
    return [i for i in range(n+1) if i % 2 == 1 ]