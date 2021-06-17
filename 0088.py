# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

# 说明:

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:

# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# 输出: [1,2,2,3,5,6]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    #2021/06/17
    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return None
        if m == 0:
            for idx,val in enumerate(nums2):
                nums1[idx] = val
            return None

        m1=m-1
        n1=n-1
        cursor = m+n-1
        while m1 > -1 and n1 > -1:
            val=0      
            if nums1[m1]<nums2[n1]:
                val = nums2[n1]
                n1-=1
                nums1[cursor]=val

                if n1 == -1:
                    return None
            else:
                val = nums1[m1]
                m1-=1
                nums1[cursor]=val

                if m1 == -1:
                    while n1>-1:
                        nums1[n1]=nums2[n1]
                        n1-=1
                    return None

            cursor-=1     
        return None
    
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for idx in range(0, n):
                nums1[idx] = nums2[idx]
            return None

        if n == 0:
            return None

        cursor1 = cursor2 = 0
        result = []        
        for num2 in nums2:
            num1 = nums1[cursor1]
            while num1 < num2 and cursor1 < m:
                result.append(num1)
                cursor1+=1
                if cursor1 < m:
                    num1 = nums1[cursor1]
            else:
                result.append(num2)
        
        while cursor1<m:
            result.append(nums1[cursor1])
            cursor1+=1

        for idx in range(0, m+n):
            nums1[idx] = result[idx]
        return None
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        c1 = c2 = 0
        l1_cp = nums1[:m]
        nums1.clear()       
        while c1<m and c2<n:
            if l1_cp[c1]<nums2[c2]:
                nums1.append(l1_cp[c1])
                c1+=1
            else:
                nums1.append(nums2[c2])
                c2+=1

        if c1<m:
            nums1[c1+c2:]=l1_cp[c1:]
        elif c2<n:
           nums1[c1+c2:]=nums2[c2:] 

        return None

solu = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solu.merge(nums1, m, nums2, n)
print(nums1)
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solu.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
solu.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0,0,3,0,0,0,0,0,0]
m = 3
nums2 = [-1,1,1,1,2,3]
n = 6
solu.merge(nums1, m, nums2, n)
print(nums1)            
