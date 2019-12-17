class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        if haystack == needle:
            return 0

        if haystack == needle == '':
            return 0

        if needle == '':
            return 0

        if haystack == '':
            return -1

        haystackList = list(haystack)
        needleList = list(needle)
        needleLen = len(needle)

        runningLoc = 0
        length = 0
        for idx, val in enumerate(haystackList):
            
            for needldIdx,needleVal in enumerate(needleList):
                # 超过父只字符串边界
                if idx+length >= len(haystack):
                    return -1

                if haystackList[idx+length] != needleVal:
                    length = 0                    
                    break
                else:
                    length+=1
                    if needldIdx == needleLen-1:
                        return idx
        return -1

solu = Solution()
haystack = "hello"
needle = "ll"
print(solu.strStr(haystack, needle))        

haystack = "mississippi"
needle = "issip"
print(solu.strStr(haystack, needle))        

haystack = "aaa"
needle = "aaaa"
print(solu.strStr(haystack, needle))        

haystack = "mississippi"
needle = "issipi"
print(solu.strStr(haystack, needle))