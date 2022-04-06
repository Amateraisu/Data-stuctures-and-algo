# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if isSameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))
    
def isSameTree(root,subRoot):
    if root is None or subRoot is None:
        return root == subRoot
    left = isSameTree(root.left, subRoot.left)
    right = isSameTree(root.right, subRoot.right)
    if root.val == subRoot.val and left and right:
        return True
    
    return False