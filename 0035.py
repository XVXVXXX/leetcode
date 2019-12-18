# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        # 二分查找
        left = 0
        right = length-1
        idx = None
        while left < right:
            idx = int((left + right) / 2)
            cntValue = nums[idx]
            
            if target > cntValue:
                left = idx+1
            elif target < cntValue:
                right = idx-1
            else:
                return idx
        if target > nums[left]:
            return left+1
        else:
            return left

solu = Solution()

nums = [1,3,5,6]
target = 5
print(solu.searchInsert(nums, target))
nums = [1,3,5,6]
target = 2
print(solu.searchInsert(nums, target))
target = 7
print(solu.searchInsert(nums, target))
target = 0
print(solu.searchInsert(nums, target))

nums = [1,3]
target = 2
print(solu.searchInsert(nums, target))