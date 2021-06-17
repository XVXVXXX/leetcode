# 169. 多数元素
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

# 示例 1:

# 输入: [3,2,3]
# 输出: 3
# 示例 2:

# 输入: [2,2,1,1,1,2,2]
# 输出: 2

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/majority-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

#2021/06/18
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stack = []
        for val in nums:
            if stack and stack[-1] != val:
                    stack.pop()
            else:
                stack.append(val)
        return stack[0]
    
class Solution:
    # hashMap 法...
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        lenth = len(nums)
        half = lenth >> 1
        for num in nums:
            count = map.get(num, 0)
            count+=1
            if count > half:
                return num
            map[num] = count

s = Solution()
nums = [2,2,1,1,1,2,2]
o = s.majorityElement(nums)
o
