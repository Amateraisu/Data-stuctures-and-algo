# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def LCA(root, node1, node2):

            if root is None:
                return None 



            left = LCA(root.left, node1, node2)
            right = LCA(root.right, node1, node2)
            if left and right:
                return root 
            
            if root.val == node1.val or root.val == node2.val:
                return root

            if left:
                return left 
            if right:
                return right 

        
        
        return LCA(root, p, q)