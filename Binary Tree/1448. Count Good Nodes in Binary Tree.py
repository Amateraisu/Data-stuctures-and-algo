# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        # O(n) time and O(h) space where n is the number of nodes and h is the height of the tree due to recursive solution 
        
        def traversal(root, greatestNumber):
            nonlocal res 
            if root is None:
                return
            
            if root.val < greatestNumber:
                # print(root.val, "1")
                traversal(root.left, greatestNumber)
                traversal(root.right, greatestNumber)
            elif root.val >= greatestNumber:
                # print(root.val, "2")
                res += 1
                traversal(root.left, root.val)
                traversal(root.right, root.val)
            

            
            return 
        traversal(root, root.val)
        return res