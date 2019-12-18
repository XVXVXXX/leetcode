# 给定两个二进制字符串，返回他们的和（用二进制表示）。

# 输入为非空字符串且只包含数字 1 和 0。

# 示例 1:

# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:

# 输入: a = "1010", b = "1011"
# 输出: "10101"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-binary
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        longList = shortList = None
        if len(a)>len(b):
            longList = list(a)
            shortList = list(b)
        else:
            longList = list(b)
            shortList = list(a)

        shortDigit = 0
        longDigit = 0

        result = []
        needCarry = 0

        longLen = len(longList)
        shortLen = len(shortList)
        for idx in range(0, longLen):
            longDigit = longList[longLen-1-idx]
            
            shortIdx = shortLen-1-idx
            if  shortIdx>=0:
                shortDigit = shortList[shortIdx]
            else:
                shortDigit = 0
            
            cntVal = int(longDigit)+int(shortDigit)+needCarry

            if cntVal>1:
                result.insert(0,str(cntVal-2))
                needCarry = 1
            else:
                result.insert(0,str(cntVal))
                needCarry = 0
        
        if needCarry:
            result.insert(0,'1')

        return ''.join(result)
        
solu = Solution()
a= '11'
b = '1'
print(solu.addBinary(a,b))