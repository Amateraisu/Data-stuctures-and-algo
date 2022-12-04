class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        res = float("inf")
        total = sum(nums)
        currentTotal = 0 
        n = len(nums)
        ret = 0
        
        for i, num in enumerate(nums):
            currentTotal += num
            first = currentTotal // (i + 1)
            last = (total - currentTotal) // (n - 1 - i) if (n - 1 - i) != 0 else 0
            
            if abs(first - last) < res:
                ret = i 
                res = abs(first - last)

        return ret