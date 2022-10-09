class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mySet = set()
        
        
        def dfs(root):
            if root is None:
                return False 
            target = k - root.val
            if target in mySet:
                return True 
            mySet.add(root.val)
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)