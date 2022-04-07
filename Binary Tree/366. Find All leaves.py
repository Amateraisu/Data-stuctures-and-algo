# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        while root:
            if root.left is None and root.right is None:
                break
            leaves = []
            findLeavesRes(root, leaves)

            res.append(leaves)
            print(res)
        res.append([root.val])
        
        return res
        
        
        
        
def findLeavesRes(root,leaves):
    if root is None:
        return
    
    if isLeaf(root.left):
        leaves.append(root.left.val)
        root.left = None
        
    if isLeaf(root.right):
        leaves.append(root.right.val)
        root.right = None
    
    findLeavesRes(root.left,leaves)
    findLeavesRes(root.right, leaves)
    

    
    return 
        
        
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False