class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # maybe we can form a number line 
        # and count the occurrances
        # Time complexity would be O(N + total)
        best = len(nums)
        length = len(nums)
        d = collections.defaultdict(int)
        delta = collections.defaultdict(int)
        maxTotal = 2 
        
        for index in range(length//2):
            maxOne = max(nums[index], nums[length - 1 - index]) + limit 
            minOne = min(nums[index], nums[length - 1 - index]) + 1
            total = nums[index] + nums[length - 1 - index]
            if maxTotal < total:
                maxTotal = total
            d[total] += 1 
            
            delta[minOne] -= 1 
            delta[maxOne + 1] += 1 
        current = length
        for total in range(2, maxTotal + 1):
            current += delta[total]
            best = min(best, current - d[total])
            
        return best