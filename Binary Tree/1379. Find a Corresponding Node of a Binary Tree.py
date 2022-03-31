# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return traverse(original, cloned, target.val)
        
        
        
def traverse(root1, root2, target):
    if root1 is None:
        return None
    if root1.val == target:
        print("match", root1.val)
        return root2
    print(root1.val, target)
    left = traverse(root1.left, root2.left, target)
    right = traverse(root1.right, root2.right, target)
    
    if left:
        return left
    else:
        return right