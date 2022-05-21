# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        prev = None 
        ptr1 = head 
        ptr2 = head 
        while ptr2:
            counter = 0
            # send ptr2 ahead to check there is enough to reverse
            while ptr2 and counter < k:
                ptr2 = ptr2.next
                counter+=1
            if counter == k:
                #reverse linked list here 
                newHead = reverseLinkedList(ptr1, k)
                # print(newHead.val)
                if prev:
                    prev.next = newHead 
                else:
                    newListHead = newHead
                
                prev = ptr1 
            else:
                prev.next = ptr1
                

                
                    
            ptr1 = ptr2
        dummy = newListHead 
        # while dummy:
        #     print(dummy.val)
        #     dummy = dummy.next
            
            
        return newListHead
                
def reverseLinkedList(node, k):
    counter = 0 
    prev = None
    current = node 
    while counter < k:
        nextNode = current.next
        current.next = prev 
        prev = current 
        current = nextNode 
        counter += 1 
    return prev 