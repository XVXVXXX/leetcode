# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return '1'

        mainQueue = ['1']
        backQueue = []

        for idx in range(1,n):
            countingChar = 0
            countingCharCount = 0
            cntChar = 0

            while len(mainQueue):
                cntChar = mainQueue.pop(0)
                if countingChar == cntChar:
                    countingCharCount+=1
                else:
                    if countingCharCount:                        
                        backQueue.append(str(countingCharCount))
                        backQueue.append(countingChar)

                    countingChar = cntChar
                    countingCharCount = 1
                
                if len(mainQueue) == 0:
                    backQueue.append(str(countingCharCount))
                    backQueue.append(countingChar)
            else:
                # switch
                tmp = mainQueue
                mainQueue = backQueue
                backQueue = tmp

        output = ''.join(mainQueue)
        return output

solu = Solution()
n = 30
print(solu.countAndSay(n))

