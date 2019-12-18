class Solution:
    def isValid(self, s: str) -> bool:
        pushList = ['(', '{', '[']
        popList = [')', '}', ']']
        dataMap = {')':'(', '}':'{', ']':'['}


        stack = []
        strList = list(s)

        for idx in range(0, len(s)):
            char = s[idx]
            if char in pushList:
                stack.append(char)
            elif char in popList:
                if len(stack) == 0:
                    return False
                poped = stack.pop()
                if poped != dataMap[char]:
                    return False

        if len(stack):
            return False                        
        return True

solu = Solution()
print(solu.isValid(']'))
print(solu.isValid('()'))
print(solu.isValid("()[]{}"))
print(solu.isValid('(]'))
print(solu.isValid('([)]'))
print(solu.isValid('{[]}'))