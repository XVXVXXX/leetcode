class Solution:
    def romanToInt(self, s: str) -> int:
        stdMap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        stdList = ['?','I','V','X','L','C','D','M']

        charList = list(s)

        poped = '?'
        lastPoped = '?'
        result = 0
        while len(charList):
            lastPoped = poped
            poped = charList.pop()
            
            if(stdList.index(poped)<stdList.index(lastPoped)):
                result = result-stdMap[poped]
            else:
                result = result+stdMap[poped]

        return result                

solu = Solution()

o = solu.romanToInt('III')
print(o)

print(solu.romanToInt('LVIII'))
