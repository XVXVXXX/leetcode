# 171. Excel表列序号
# 给定一个Excel表格中的列名称，返回其相应的列序号。

# 例如，

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# 示例 1:

# 输入: "A"
# 输出: 1
# 示例 2:

# 输入: "AB"
# 输出: 28
# 示例 3:

# 输入: "ZY"
# 输出: 701

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/excel-sheet-column-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    ASICII_A = 65
    notation = 26
    def titleToNumber(self, s: str) -> int:
        retVal = 0
        length = len(s)
        for i in range(0, length):
            char = s[length-1-i]
            num = ord(char)-self.ASICII_A+1
            num = num * pow(26, i)
            retVal += num
        return retVal

s = Solution()
o = s.titleToNumber("AB")