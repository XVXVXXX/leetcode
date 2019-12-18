# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:

# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/plus-one
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        for idx in range(len(digits)-1,-1,-1):
            digit = digits[idx]
            if digit+1<10:
                digits[idx]=digit+1
                return digits
            else:
                digits[idx]=0
        digits.insert(0,1)
        return digits


    def plusOne1(self, digits: List[int]) -> List[int]:
        inputNum = digits[0]
        for idx in range(1, len(digits)):
            inputNum = inputNum*10 + digits[idx]
        return list(str(inputNum+1))

solu = Solution()
digits = [1,2,3,4]
print(solu.plusOne(digits))        
digits = [1,2,3]
print(solu.plusOne(digits))
digits = [9]
print(solu.plusOne(digits))