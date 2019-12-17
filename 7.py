class Solution:
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

        if(output<-1*pow(2,31) or output>=pow(2,31)):
            return 0      

        return output
    
solu = Solution()
o = solu.reverse(1534236469)
print(o)

o = solu.reverse(-123)
print(o)