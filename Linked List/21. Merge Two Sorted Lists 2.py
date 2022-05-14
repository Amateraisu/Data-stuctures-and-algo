# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         if not list1 and not list2:
#             return None
#         elif not list1:
#             return list2
#         elif not list2:
#             return list1
#         else:
            
#             ptr1 = list1
#             ptr2 = list2

#             #determine the starting node 
#             if ptr1.val < ptr2.val:
#                 current = ptr1
#                 ptr1 = ptr1.next
#                 result = current
#             else:
#                 current = ptr2
#                 ptr2 = ptr2.next
#                 result = current

#             while ptr1 and ptr2:
#                 if ptr1.val < ptr2.val:
#                     current.next = ptr1
#                     ptr1 = ptr1.next
#                 else:
#                     current.next = ptr2
#                     ptr2 = ptr2.next
#                 current = current.next

#             # edge case in case ptr1 or ptr2 still have nodes remaining 
#             while ptr1: 
#                 current.next = ptr1 
#                 current = current.next
#                 ptr1 = ptr1.next
#             while ptr2:
#                 current.next = ptr2
#                 current = current.next
#                 ptr2 = ptr2.next

#             return result
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2