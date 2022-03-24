# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentPtr = root
        
        while currentPtr is not None:
            if p.val > currentPtr.val and q.val > currentPtr.val:
                currentPtr = currentPtr.right
            elif p.val < currentPtr.val and q.val < currentPtr.val:
                currentPtr = currentPtr.left
            else:
                break
                
                
        return currentPtr