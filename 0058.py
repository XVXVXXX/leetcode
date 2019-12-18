# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 示例:

# 输入: "Hello World"
# 输出: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        didFindChar = False
        length = 0
        for idx in range(len(s)-1, -1, -1):
            cnt = s[idx]
            if cnt != ' ':
                didFindChar = True
                length += 1
            elif didFindChar:
                return length

        if didFindChar == False:
            return 0
        else:
            return length

solu = Solution()
s = 'a'
print(solu.lengthOfLastWord(s))
        
