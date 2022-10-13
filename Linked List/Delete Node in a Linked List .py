# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ptr = node 
        prev = None 
        
        while ptr:
            next = ptr.next 
            if next != None:
                
                ptr.val = next.val 
            else:
                
                prev.next = None
            prev = ptr 
            ptr = ptr.next
        return