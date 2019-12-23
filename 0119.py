# 杨辉三角
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:      
        lastList = [1]
        for i in range(1, rowIndex+1+1):
            cntList = [None] * i
            cntList[0] = cntList[i-1] = 1
            for j in range(1, (i+1)>>1):
                val = lastList[j] + lastList[j-1]
                cntList[j] = cntList[i-j-1] = val

            lastList = cntList
    
        return lastList

n = 5
so = Solution()
o = so.generate(5)
o