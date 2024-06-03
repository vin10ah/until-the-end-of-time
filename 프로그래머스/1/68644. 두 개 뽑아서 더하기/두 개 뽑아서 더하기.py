# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(len(numbers[i:])):
#             if (numbers[i] + numbers[j]) not in answer:
#                 answer.append(numbers[i] + numbers[j])
#     return answer

from itertools import combinations

def solution(numbers):
    answer = set()
    for comb in combinations(numbers, 2):
        answer.add(sum(comb))
    
    return sorted(list(answer))