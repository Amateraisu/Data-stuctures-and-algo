# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        return sumOfLeftLeavesHelper(root)
    
    
def sumOfLeftLeavesHelper(root):
    if root is None:
        return 0
    left = sumOfLeftLeavesHelper(root.left)
    right = sumOfLeftLeavesHelper(root.right)
    
    
    if root.left:
        if root.left.right == None and root.left.left == None:
            return left+ right+root.left.val
    return left+ right