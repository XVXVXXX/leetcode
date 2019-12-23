# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

# 说明: 叶子节点是指没有子节点的节点。

# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


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
    # 迭代 DFS
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        node = root
        val = root.val
        stack = []
        while (node and val != None) or len(stack):
            if node:
                if not node.left and not node.right and val == sum:
                    return True 

                stack.append(tuple((node, val)))

                node = node.left
                if node:
                    val = val+node.val
            else:
                lastNode, lastVal = stack.pop()
                node = lastNode.right
                if node:
                    val = lastVal + node.val
        return False

    # 递归
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root:
            if not root.left and not root.right and sum == root.val:
                return True
        else:
            return False
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
nums = [1]
nums = [0,1,1]
tree = setupTree(nums)

so = Solution()
o = so.hasPathSum(tree, 1)
o
