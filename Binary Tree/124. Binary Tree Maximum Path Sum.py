# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        
        def findMaxPath(root):
            nonlocal res
            if root is None:
                return 0 
            left = findMaxPath(root.left)
            right = findMaxPath(root.right)
            # evaluate max sum here 
            
            if left <= 0 and right <= 0:
                res = max(res, root.val)
                
                return root.val
            elif left <= 0 and right >= 0:
                res = max(root.val + right, res)
                
                return root.val + right 
            elif left >= 0 and right <= 0:
                res = max(root.val + left, res)
                return root.val + left 
            elif left >= 0 and right >= 0:
                res = max(left + right + root.val , res)
                return max(left, right) + root.val
            
        findMaxPath(root)
        return res