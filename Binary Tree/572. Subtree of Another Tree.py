# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot):
            return True
        
        
        
        return isSubTreeHelper(root, subRoot)
    
    
def isSubTreeHelper(root, root2):
    if root is None or root2 is None:
        return root == root2
    
    if root.val == root2.val and isSubTreeHelper(root.left, root2.left) and isSubTreeHelper(root.right, root2.right):
        return True
    
    return False