# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        return isSame(root, subRoot)
    
    
    
    
def isSame(root1, root2):
    if root1 is None or root2 is None:
        return root1 == root2
    
    
    left = isSame(root1.left, root2)
    right = isSame(root1.right, root2)
    current = False 
    if root2.val == root1.val:
        # issame Tree 
        current = isSameTree(root1, root2)
    return left or right or current
    
        
def isSameTree(root1, root2):
    if root1 is None or root2 is None:
        return root1 == root2
    
    return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right) and root1.val == root2.val 