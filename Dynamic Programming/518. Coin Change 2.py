class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # time complexity will be O(m*n) 
        # space complexity will also be O(m*n)
        dpArray = [[0 for cost in range(amount+1)] for coin in coins]
        for coin in range(len(coins)):
            dpArray[coin][0] = 1

        

        for cost in range(1, amount+1):
            for indexOfCoin in range(len(coins)):
                currentCoin = coins[indexOfCoin]
                target = cost - currentCoin
                if indexOfCoin > 0 and  target < 0:
                    dpArray[indexOfCoin][cost] = dpArray[indexOfCoin-1][cost]
                elif target >=0 and indexOfCoin > 0:
                    dpArray[indexOfCoin][cost] = dpArray[indexOfCoin-1][cost] + dpArray[indexOfCoin][target]
                elif target >= 0: #at the top row 
                    dpArray[indexOfCoin][cost] = dpArray[indexOfCoin][target]
        
        
        return dpArray[len(coins)-1][amount]