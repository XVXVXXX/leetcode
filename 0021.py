# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1

        cursorNode = l1
        standByNode = l2

        if cursorNode.val>standByNode.val:
            tmp = cursorNode
            cursorNode = standByNode
            standByNode = tmp

        outputListNode = cursorNode

        while cursorNode.next != None:
            if cursorNode.next.val>standByNode.val:
                tmp = cursorNode.next
                cursorNode.next = standByNode

                standByNode = tmp

            cursorNode =  cursorNode.next
        
        if standByNode != None:
            cursorNode.next = standByNode

        return outputListNode


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

solu = Solution()
i = solu.mergeTwoLists(l1, l2)

l1 = None
l2 = None
i = solu.mergeTwoLists(l1, l2)

j = None