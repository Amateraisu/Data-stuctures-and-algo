class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashmap = {}
        
        
        def traverse(root, hashmap):
            if root is None:
                return

            if root.val not in hashmap.keys():
                hashmap[root.val] = 1



            else:
                hashmap[root.val] +=1

            traverse(root.left, hashmap)
            traverse(root.right, hashmap)

        traverse(root, hashmap)
        return [key for key, value in hashmap.items() if value == max(hashmap.values())]