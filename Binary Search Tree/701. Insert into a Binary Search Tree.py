# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        lastDirection = None 
        
        parent = None 
        currentPtr = root
        while currentPtr:
            if currentPtr.val > val:
                parent = currentPtr
                currentPtr = currentPtr.left
                lastDirection = "L"
            elif currentPtr.val < val:
                parent = currentPtr 
                currentPtr = currentPtr.right
                lastDirection = "R"
            else:
                parent = currentPtr 
                currentPtr = currentPtr.right 
                lastDirection = "R"
                
        if lastDirection == "R":
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
            
        return root 