class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        tortoise = head 
        prev = None 
        hare = head 
        
        while hare and hare.next != None:
            prev = tortoise 
            tortoise = tortoise.next
            hare = hare.next.next 
        
        prev.next = tortoise.next 
        return head 