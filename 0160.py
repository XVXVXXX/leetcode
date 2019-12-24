# 160. 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。

# 如下面的两个链表：

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # stack
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        stackA = []
        nodeA = headA
        while nodeA:
            stackA.append(nodeA)
            nodeA = nodeA.next
        lenA = len(stackA)

        stackB = []
        nodeB = headB
        while nodeB:
            stackB.append(nodeB)
            nodeB = nodeB.next
        lenB = len(stackB)

        lastCommonNode = None
        while len(stackA) and len(stackB):
            tailA = stackA.pop()
            tailB = stackB.pop()
            if tailA == tailB:
                lastCommonNode = tailA
            else:
                break
        
        return lastCommonNode
        

