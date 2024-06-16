import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        asc_nums = []
        for i in range(len(nums)):
            heapq.heappush(asc_nums, -nums[i])
            
        for i in range(k):
            if i == k-1:
                return -heapq.heappop(asc_nums)
            else:
                heapq.heappop(asc_nums)

                
                