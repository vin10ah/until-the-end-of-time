# def solution(numbers, target):
#     answer = 0
#     def dfs(i,total):
#         if i == len(numbers):
#             if total == target:
#                 answer += 1
#         else:
#             dfs(i+1, tota)
        
        
#     return answer

# def solution(numbers, target):
#     answer = 0
#     for i in range(len(numbers)):
#         ntarget = target - numbers[i]

        
        
def solution(nums, target):
    answer = 0
    n = len(nums)
    count = [0]
    
    def dfs(idx, x=0):
        if idx == n:
            if x == target:
                count[0] += 1
            return
        
        for num in (nums[idx], -nums[idx]):
            dfs(idx+1, x+num)
            
    dfs(0)
    
    return count[0]
        
                