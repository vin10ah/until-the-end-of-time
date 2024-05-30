# def solution(n, numlist):
#     answer = []
#     for num in numlist:
#         if num % n == 0:
#             answer.append(num)
#     return answer


# def solution(n, numlist):
#     for num in numlist:
#         if num % n != 0:
#             numlist.remove(num)
#     return numlist

def solution(n, numlist):

    return list(filter(lambda x: x % n==0, numlist))