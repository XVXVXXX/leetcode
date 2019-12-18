# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # min value
        maxVal = nums[0]
        collectingMax = maxVal

        for val in nums[1:]:
            if collectingMax < 0:                
                collectingMax = val
            else: #>=0
                collectingMax = collectingMax + val
                
            if collectingMax>maxVal:
                maxVal = collectingMax
        
        return maxVal

solu = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solu.maxSubArray(nums))