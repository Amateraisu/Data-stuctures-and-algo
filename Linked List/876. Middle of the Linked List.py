class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head
        
        while ptr2 != None and ptr2.next != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            
        return ptr1