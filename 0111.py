# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:

# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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
    # 递归
    def minDepth1(self, root: TreeNode) -> int:
        # only for []
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1

        if root.left:
            return self.minDepth(root.left)+1
        if root.right:
            return self.minDepth(root.right)+1

    # 迭代 有点像DFS 但并不是纯粹的DFS
    def minDepth11(self, root: TreeNode) -> int:

        if not root:
            return 0

        minDepth = float('inf')
        stack = [tuple((root, 1))]
        cntDepth = float('inf')

        while stack:
            node, depth = stack.pop()
            left = node.left
            right = node.right

            if not left and not right:
                minDepth = min(depth, minDepth)
                continue

            if left:
                stack.append(tuple((left, depth+1)))
            if right:
                stack.append(tuple((right, depth+1)))
        
        return minDepth

    # BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [root]
        minDepth = 0
        while queue:
            minDepth += 1

            length = len(queue)
            newQueue = []
            for idx in range(0, length):
                node = queue[idx]
                if not node.left and not node.right:
                    return minDepth
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)

            queue = newQueue
        return minDepth


nums = [3,9,20,None,None,15,7]
tree = setupTree(nums)
o = Solution().minDepth(tree)
print(o)