class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        visited = collections.defaultdict(int)
        for num in nums:
            tot = int(max(list(str(num)), key=lambda x: int(x)))

            if tot in visited:
                res = max(res, num + visited[tot])
                visited[tot] = max(visited[tot], num)
            else:
                visited[tot] = num
            # print(num, tot, res)

        return res