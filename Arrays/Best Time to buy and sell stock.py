class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force approach 
        # Time complexity is O(n^2) and space O(1) space complexity 
#         profit = 0
        
#         for index in range(0, len(prices)):
#             for index2 in range(index, len(prices)):
#                 currentProfit = prices[index2] - prices[index]
                
#                 if currentProfit>profit:
#                     profit = currentProfit
                    
                    
#         return profit
        #time complexity O(n) and space O(1)
    
        ptr1 = 0
        ptr2 = 1
        
        maxProfit = 0
        
        while ptr2<=len(prices)-1:
            if prices[ptr2]<prices[ptr1]:
                ptr1 = ptr2
                ptr2 +=1
            else:
                currentProfit = prices[ptr2] - prices[ptr1]
                if currentProfit > maxProfit:
                    maxProfit = currentProfit
                
                ptr2+=1
                
        return maxProfit