# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(N)

        numberOfNodes = self.getNum(root)
        
        res = [[] for i in range(numberOfNodes)]
        
        def postOrder(root):
            if root is None:
                return 0 
            
            left = postOrder(root.left)
            right = postOrder(root.right)
            
            res[max(left, right)].append(root.val)
            # print(root.val, max(left, right), res)
            return max(left, right) + 1
            

            
        postOrder(root)
        while res and len(res[-1]) == 0:
            res.pop()
        return res 
    
    def getNum(self,root):
        if root is None:
            return 0 
        left = self.getNum(root.left)
        right = self.getNum(root.right)
        
        return 1 + left + right