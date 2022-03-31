# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # I need to do a level order traversal 
        
        # Breadth First Search 
        
        if root is None:
            return []
        
        queue = []
        res = []
        
        queue.append(root)
        
        while len(queue) > 0:
            level_sum = 0
            size = len(queue)
            
            for node in range(size):
                currentNode = queue.pop(0)
                level_sum += currentNode.val
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)
            average = level_sum / (size)
            res.append(average)
        
        return res