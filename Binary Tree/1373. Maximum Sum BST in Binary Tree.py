# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # a few observations is that every leaf node is also a bst

        # we can do a post order traversal
        # so for every node, return whether it is a BST or not
        # for every node, return the smallest and largest range of the node
        # and for every node, check that it is smaller than the smallest on the right
        # and check that it is larger than every node on the left
        # if it fulfills the condition, then add all the sums together,
        # if it DOESNT fulfill the condition, then set impossible boundaries for the subtree
        # such as [float("-inf"), float("inf")]

        # but for a root node, return [float("inf"), float("-inf")]
        res =0
        def dfs(node):
            nonlocal res
            if node is None:
                return [float("inf"), 0, float("-inf")]

            l, r = dfs(node.left), dfs(node.right)
            if node.val > l[2] and node.val < r[0]:
                res = max(res, node.val + l[1] + r[1])

            else:
                return [float("-inf"), 0, float("inf")]

            return [min(l[0], r[0], node.val) , node.val + l[1] + r[1], max(l[2], r[2], node.val)]


        dfs(root)
        return res
