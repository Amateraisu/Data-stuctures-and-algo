# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # construct id for every single node 
        maps = defaultdict(int)
        res = []
        
        def dfs(node):
            if node is None:
                return "*"
            currentID = dfs(node.left) + "," + dfs(node.right) + "," + str(node.val)

            if currentID in maps and maps[currentID] == 1:
                res.append(node)
            maps[currentID] += 1

            return currentID
        dfs(root)

        return res