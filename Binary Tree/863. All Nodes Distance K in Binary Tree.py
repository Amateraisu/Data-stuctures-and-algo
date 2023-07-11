# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        # how do I calculate this distance? obviously its child will be easy.
        # but how do I calculate say, its parents?
        # for parents, lets say k = 2
        # so there is the parent and then... repeat for that
        # From the root to the target, all the nodes on the other side is guaranteed to be + 1
        # then as I get closer, - 1
        # Preorder Root L R
        # Inorder L Root R
        # Post order L R Root
        # then what if for every node, record the distance away from the target?
        # first count the distance of the root from the target
        # transform this tree into a graph
        # then do a dfs
        graph = collections.defaultdict(set)
        start = None

        def dfs(node):

            if node.left:
                graph[node].add(node.left)
                graph[node.left].add(node)
                dfs(node.left)
            if node.right:
                graph[node].add(node.right)
                graph[node.right].add(node)
                dfs(node.right)
            return

        dfs(root)
        visited = set()

        def dfs2(node, dist):
            if dist == k:
                res.append(node.val)
                return
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs2(nei, dist + 1)
            return

        dfs2(target, 0)
        return res


