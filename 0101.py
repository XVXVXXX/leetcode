# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    def isTwoTreeSymmetric(self, p: TreeNode, q: TreeNode) -> bool:
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            return p.val == q.val and self.isTwoTreeSymmetric(p.left, q.right) and self.isTwoTreeSymmetric(p.right, q.left)

    def isSymmetric1(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isTwoTreeSymmetric(root.left, root.right)

        # 循环
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        p = root.left
        q = root.right

        if p == None and q == None:
            return True
        if p == None or q == None:
            return False


        pStack = [None]
        qStatck = [None]

        while (p and q) or (len(pStack)):
    
            if p and q:
                if p.val != q.val:
                   return False

                pStack.append(p.left)
                pStack.append(p.right)

                qStatck.append(q.right)
                qStatck.append(q.left)
            elif p != None or q != None:
                # p / q 中有一个为 None
                return False

            if len(pStack):
                p = pStack.pop(0)
                q = qStatck.pop(0)
            
        return True

def setupTree(nums: list) -> TreeNode:
    stack = []
    root = TreeNode(nums[0])
    stack.append(root)
    locateInLeft = True
    for num in nums[1:]:
        node = None
        if num:
            node = TreeNode(num)
            stack.append(node)

        top = stack[0]
        if locateInLeft:
            top.left = node
        else:
            top.right = node
            stack.pop(0)
        locateInLeft = not locateInLeft
    
    return root

so = Solution()


nums = [1,2,2,None,3,None,3]
tree = setupTree(nums)
out = so.isSymmetric(tree)
print(out)