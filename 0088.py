# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

# 说明:

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:

# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# 输出: [1,2,2,3,5,6]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # idx1 = idx2 = 0
        # cursorIdx = 0
        # while cursorIdx<m+n:
        #     if nums1[idx1] >=  nums2[idx2]:
        #         pass
        i = 0

        if len(nums1) == 1:
            if nums1[0] == 0:
                nums1[0] = nums2[0]
            return

        for num2 in nums2:
            loc = self.searchInsert(nums1[0:m+i], num2)
            nums1.insert(loc, num2)
            nums1.pop(-1)
            i+=1

    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

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
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solu.merge(nums1, m, nums2, n)
print(nums1)
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solu.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
solu.merge(nums1, m, nums2, n)
print(nums1)