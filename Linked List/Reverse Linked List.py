class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # so there is 2 ways of reversing a linked List.
        # O(n) time and O(1) space where n is the length of the linked list 
        
#         current = head 
#         res = []
#         prev = nextPtr = None 
#         while current:
#             nextPtr = current.next
#             current.next = prev
#             prev = current 
#             current = nextPtr
            
            
        
#         return prev
        if not head:
            return None
        
        newHead = head 
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None
        
        return newHead 