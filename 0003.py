# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        maxLen = 0
        for char in s:
            if char in queue:
                idx = queue.index(char)
                queue = queue[idx+1:]
            queue.append(char)
            maxLen = max(len(queue), maxLen)
            
        return maxLen

so = Solution()
s = "abcabcbb"
o = (so.lengthOfLongestSubstring(s))
print(o)
