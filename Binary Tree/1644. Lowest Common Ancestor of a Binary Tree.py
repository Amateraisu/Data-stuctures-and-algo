# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(node) -> bool:
            nonlocal res
            if not node:
                return False
            s = 0
            cur = False
            if node.val == p.val or node.val == q.val:
                cur = True
                s = 1
            l = dfs(node.left)
            if l:
                s += 1
            r = dfs(node.right)
            if r:
                s += 1
            cur = cur or l or r
            if s >= 2:
                res = node
            return cur
        dfs(root)
        return res