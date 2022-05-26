# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upperLimit = float("inf")
        lowerLimit = float("-inf")
        return isValid(root, upperLimit, lowerLimit)
    
    
    
def isValid(root, upperLimit, lowerLimit):
    if root is None:
        return True
    
    return isValid(root.left, root.val, lowerLimit) and isValid(root.right, upperLimit, root.val) and root.val < upperLimit and root.val > lowerLimit