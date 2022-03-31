# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # start at the root 
        
        if len(nums) == 0:
            return None
        
        else:
            return constructTreeFromArray(nums, 0 , len(nums)-1)
        
        
def constructTreeFromArray(nums, left, right):
    if left > right:
        return None
    midpoint = left + (right-left) // 2
    node = TreeNode(nums[midpoint])
    node.left = constructTreeFromArray(nums, left, midpoint-1)
    node.right = constructTreeFromArray(nums, midpoint+1, right)
    return node