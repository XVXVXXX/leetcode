# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：

# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def setupTree(nums: list) -> TreeNode:
    queue = []
    root = TreeNode(nums[0])
    queue.append(root)
    locateInLeft = True
    for num in nums[1:]:
        node = None
        if num:
            node = TreeNode(num)
            queue.append(node)

        head = queue[0]
        if locateInLeft:
            head.left = node
        else:
            head.right = node
            queue.pop(0)
        locateInLeft = not locateInLeft
    
    return root        

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = []
        queue.append(root)
        queue.append(None)

        retVal = []
        innerList = []
        retVal.append(innerList)

        while len(queue):
            head = queue.pop(0)
            if head == None:
                # 如果一个都没有了，就说明结束了
                if len(queue) == 0:
                    break

                innerList = []
                retVal.append(innerList)
                queue.append(None)
                continue
            else:
                innerList.append(head.val)
            
            if head.left:
                queue.append(head.left)
            if head.right:
                queue.append(head.right)
        
        retVal.reverse()
        return retVal

nums = [3,9,20,None,None,15,7]
tree = setupTree(nums)


solu = Solution()
output = solu.levelOrderBottom(tree)
output

            


