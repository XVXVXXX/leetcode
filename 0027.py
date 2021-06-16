from typing import List

class Solution:
    #2021/6/16
    def removeElement(self, nums: List[int], val: int) -> int:
        cursor = 0
        for idx, num in enumerate(nums):
            if num == val:
                continue
            else:
                nums[cursor] = num
                cursor+=1

        return cursor
    
    def removeElement1(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        
        leftIdx = 0
        rightIdx = 0

        while rightIdx < len(nums):
            ctnVal = nums[rightIdx]
            if ctnVal != val:
                nums[leftIdx] = ctnVal
                leftIdx = leftIdx+1
            rightIdx = rightIdx+1

        return leftIdx

solu = Solution()
nums = [3,2,2,3]
val = 3
print(solu.removeElement(nums, val))        
nums = [0,1,2,2,3,0,4,2]
val = 2
print(solu.removeElement(nums, val))        

nums = []
val = 1
print(solu.removeElement(nums, val))        
