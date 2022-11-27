# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        ptr = head 
        while ptr:
            currentValue = ptr.val 
            while stack and currentValue > stack[-1]:
                stack.pop()
                
                
            stack.append(currentValue)
            ptr = ptr.next 
            

        ptr = head 
        prev = None 
        ptr1 = 0 
        while ptr1 < len(stack):

            ptr.val = stack[ptr1]
            ptr1 += 1 
            prev = ptr
            ptr = ptr.next 
        prev.next = None
        
        
        return head 