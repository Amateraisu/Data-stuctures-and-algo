# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return inOrderTraversal(root)-1
        
        
def inOrderTraversal(root):
    if root is None:
        return 0
    left = inOrderTraversal(root.left)
    middle = 1 + getSubHeight(root.left) + getSubHeight(root.right)
    right = inOrderTraversal(root.right)

    return max(left,middle,right)


def getSubHeight(root):
    if root is None:
        return 0
    left = getSubHeight(root.left) + 1 
    right = getSubHeight(root.right) + 1
    
    return max(left,right)