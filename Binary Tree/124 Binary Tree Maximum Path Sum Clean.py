# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")


        def dfs(node):
            nonlocal res
            if node is None:
                return 0 

            left = dfs(node.left)
            right = dfs(node.right)
            current = node.val
            res = max(res, current + left + right, current, current + left, current + right)
            toReturn = max(left + current, right + current, current)

            return toReturn 

        dfs(root)

        return res