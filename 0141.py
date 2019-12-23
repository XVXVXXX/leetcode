# 141. 环形链表
# 给定一个链表，判断链表中是否有环。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        fastNode = head
        slowNode = head

        while fastNode and fastNode.next:
            fastNode = fastNode.next.next
            slowNode = slowNode.next
            if fastNode == slowNode:
                return True
        return False