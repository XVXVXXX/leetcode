# 167. 两数之和 II - 输入有序数组
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

# 说明:

# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

#2021/06/17
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            diff = numbers[l]+numbers[r]-target
            if diff < 0:
                l+=1
            elif diff > 0:
                r-=1
            else:
                return [l+1,r+1]
        return [l+1,r+1]


class Solution:
    # 双指针
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        left = 0
        right = len(numbers)-1

        while left < right:
            leftVal = numbers[left]
            rightVal = numbers[right]

            cntSum = leftVal + rightVal
            if cntSum == target:
                # 需求中，下标是从1开始
                return [left+1, right+1]
            if cntSum > target:
                right-=1
            else:
                left+=1
            
        return None

s = Solution()
nums = [2, 7, 11, 15]
target = 9
o = s.twoSum(nums, target)
o
