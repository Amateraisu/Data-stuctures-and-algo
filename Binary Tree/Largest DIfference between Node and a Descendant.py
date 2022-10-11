# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # do a dfs and find the maximum minimum of that traversal and then store it in res

        res = 0 

        def dfs(node, maximum, minimum):
            nonlocal res
            if node is None:

                res = max(res, maximum - minimum)
                return 

            dfs(node.left, max(maximum, node.val), min(minimum, node.val))
            dfs(node.right, max(maximum, node.val), min(minimum, node.val))

            return 
        dfs(root, float("-inf"), float("inf"))
        return res