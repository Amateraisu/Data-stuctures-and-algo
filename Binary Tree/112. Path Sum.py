# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case is if there is a target met 
        if root is None:
            return False
        return pathSumHelper(root, targetSum, 0)
    
    # I need a function that traverse the tree and sum it 
    
    # inorder traversal 
    # if i found it , return 
    
def pathSumHelper(root, targetSum, currentSum):
    if root is None: 
        return False
    currentSum += root.val
    if root.left is None and root.right is None and targetSum == currentSum:
        return True
    
    
    left = pathSumHelper(root.left, targetSum, currentSum)
    right = pathSumHelper(root.right, targetSum, currentSum)
    
    if left or right:
        return True
    
    return False