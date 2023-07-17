# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        l1 = reverse(l1)
        l2 = reverse(l2)
        c = 0
        dummy = ListNode()
        ptr = dummy
        while l1 or l2 or c:
            s1 = l1.val if l1 else 0
            s2 = l2.val if l2 else 0
            cur = (s1 + s2 + c)
            n = (s1 + s2 + c) % 10
            ptr.next = ListNode(n)
            if cur >= 10:
                c = 1
            else:
                c = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            ptr = ptr.next
        nex = dummy.next
        dummy.next = None
        return reverse(nex)


def reverse(root):
    prev = None
    cur = root
    while root:
        nex = root.next
        root.next = prev
        prev = root
        root = nex
    return prev