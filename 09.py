class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        if(x==0):
            return True
        
        if(x == self.reverse(x)):
            return True
        return False

    def reverse(self, x: int) -> int:
        isPositive = 1
        if(x<0):
            isPositive = -1

        absVal = isPositive * x

        cntVal = 0
        output = 0

        while absVal>0:            
            cntVal = absVal%10
            absVal = int(absVal/10)
            output = output*10+cntVal

        output = isPositive * output

        return output
