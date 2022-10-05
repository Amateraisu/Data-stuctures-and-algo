# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            
            newNode.left = root
            
            return newNode 
        
        queue = deque()
        queue.append([root, 1])
        while queue:
            currentLength = len(queue)
            
            for i in range(currentLength):
                currentNode, currentDepth = queue.popleft()
                tempList = [currentNode.left, currentNode.right]
                if currentDepth == depth - 1:
                    # keep track of left and right nodes and make new child nodes 
                    
                    currentNode.left = TreeNode(val)
                    currentNode.right = TreeNode(val)
                    currentNode.left.left = tempList[0]
                    currentNode.right.right = tempList[1]
                
                # append the node's children 
                if tempList[0]:
                    
                    queue.append([tempList[0], currentDepth + 1])
                if tempList[1]:
                    queue.append([tempList[1], currentDepth + 1])
                    
        return root