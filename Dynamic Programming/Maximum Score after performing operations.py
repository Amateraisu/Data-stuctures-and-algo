
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # I will throw my nums into a queue to easy pop front or pop back 
        # everytime I do an operation I can consider 
        # I can choose to either pop front or pop back to add to my total score 
        
        
        # when multipliers == 0:
        # thats when I reached my end condition 
        # O(N^2) time and space 
        N = len(nums)
        cache = {}
        def dfs(i , j, multipliersIndex):
            if multipliersIndex == len(multipliers):
                return 0
            if i > j:
                return float("-inf")
            
            
            if (i, j, multipliersIndex) in cache:
                return cache[(i, j, multipliersIndex)]

            temp = 0
            # take from the front 
            frontElement = nums[i]
            backElement = nums[j]
            left = frontElement * multipliers[multipliersIndex] + dfs(i + 1, j , multipliersIndex + 1)
            
            # take from the back 
            right = backElement * multipliers[multipliersIndex] + dfs(i, j - 1, multipliersIndex + 1)
            
            cache[(i, j, multipliersIndex)] = max(left, right)
            
            return cache[(i, j, multipliersIndex)]

        return dfs(0, N - 1, 0 )