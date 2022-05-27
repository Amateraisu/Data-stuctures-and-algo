# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        return buildTreeTraversal(preorder, inorder)
    
    
    
    
def buildTreeTraversal(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    root = TreeNode(preorder[0])
    indexOfRoot = inorder.index(preorder[0])
    preOrderLeft = preorder[1:indexOfRoot + 1]
    
    preOrderRight = preorder[indexOfRoot+1:]
    inOrderLeft = inorder[:indexOfRoot]
    inOrderRight = inorder[indexOfRoot+1:]
    
    root.left = buildTreeTraversal(preOrderLeft, inOrderLeft)
    root.right = buildTreeTraversal(preOrderRight, inOrderRight)
    
    return root