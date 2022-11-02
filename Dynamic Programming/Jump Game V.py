class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        
        res = [0] * len(arr)
        @cache
        def dfs(index):


            res = 1 

            for i in range(index + 1, min(index + 1 + d, len(arr))):
                if arr[i] >= arr[index]:
                    break 
                res = max(res, dfs(i) + 1)

            for j in range(index - 1, max(index - 1 -d, -1) , -1):
                if arr[j] >= arr[index]:
                    break 
                res = max(res, dfs(j) + 1)

            return res 




        for i in range(len(arr)):
            res[i] = dfs(i)
        
        return max(res)