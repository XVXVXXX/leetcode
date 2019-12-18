from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        #max value
        minLen = 1000000
        for aStr in strs:
            currentLen = len(aStr)
            if currentLen < minLen:
                minLen = currentLen

        if minLen == 0:
            return ''

        lastLoc = 0

        for loc in range(0, minLen):
            char = strs[0][loc]

            thisCharCommon = False
            for idx, val in enumerate(strs):
                if val[loc] != char:
                    thisCharCommon = False
                    break
                else:
                    thisCharCommon = True
            if thisCharCommon:
                lastLoc = lastLoc+1
            else:
                break

        if lastLoc>0:
            return strs[0][0:lastLoc]
        else:
            return ''

solu = Solution()
print(solu.longestCommonPrefix(["a"]))