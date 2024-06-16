class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for num1 in nums:
            num2 = target-num1
            i = nums.index(num1)+1
            if num2 not in nums[i:]:
                continue
            else:
                answer.append(nums.index(num1))
                answer.append(nums.index(num2,i))
                return answer

                
        

        