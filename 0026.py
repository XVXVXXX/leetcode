from typing import List
class Solution:
    # 2021/6/16
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        
        count = 0
        for idx, val in enumerate(nums):
            if nums[count] == val:
                continue
            else:
                count=count+1
                nums[count]=val
        
        return count+1
    
    # 2020
    def removeDuplicates1(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        
        leftIdx = 0
        rightIdx = 0
        lastVal = nums[leftIdx]

        while rightIdx < len(nums):
            val = nums[rightIdx]
            if val != lastVal:
                leftIdx = leftIdx+1
                nums[leftIdx] = val
                lastVal = val
            rightIdx = rightIdx+1

        return leftIdx+1

solu = Solution()
nums = [1,1,2]
print(solu.removeDuplicates(nums))        
nums = [0,0,1,1,1,2,2,3,3,4]
print(solu.removeDuplicates(nums))        
