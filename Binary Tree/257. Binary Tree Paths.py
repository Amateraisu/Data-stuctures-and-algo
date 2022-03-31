# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        emptyString = ""
        
        
        binaryTreePathsHelper(root, emptyString, res)
        print(res)
        
        
        
        
        
        return res 

    
def binaryTreePathsHelper(node, emptyString, res):
    emptyString += str(node.val)
    if node.left is None and node.right is None:
        res.append(emptyString)
        return 
    
    if node.left is not None: 
        binaryTreePathsHelper(node.left, emptyString + "->", res)
    if node.right is not None:
        binaryTreePathsHelper(node.right, emptyString + "->", res)
        
    return 