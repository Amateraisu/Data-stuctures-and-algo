class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [-1]
        stack = [[0, nums[0]]]
        ans = [-1] * len(nums)
        
        for i in range(1, len(nums)):
            currentNumber = nums[i]
            while stack and currentNumber > stack[-1][1]:
                ans[stack[-1][0]] = currentNumber
                stack.pop()
            stack.append([i, currentNumber])
        
        for index, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                ans[stack[-1][0]] = num 
                stack.pop()
                
        return ans