# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        cache = collections.defaultdict(int)

        # do a postorder traversal to make it into smaller sub problems

        def dfs(currentNode):
            if not currentNode:
                return 0

            cache[(currentNode, "L")] += dfs(currentNode.left) + cache[(currentNode.left, "R")]
            cache[(currentNode, "R")] += dfs(currentNode.right) + cache[(currentNode.right, "L")]

            return 1

        dfs(root)

        return max(cache.values())




