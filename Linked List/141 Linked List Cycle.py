class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #so in order to detect a cycle, we can use floyd's haire and tortoise algorithm
        
        rabbit = head
        tortoise = head
        
        while rabbit != None and rabbit.next != None:
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if tortoise == rabbit:
                return True
        
        return False