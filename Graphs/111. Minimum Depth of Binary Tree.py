# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        if not root:
            return 0
        q = deque()
        q.append([root, 1])
        while q:
            f, h = q.popleft()
            if not f.left and not f.right:
                res = min(res, h)
            if f.left:
                q.append([f.left, h + 1])
            if f.right:
                q.append([f.right, h + 1])
        return res