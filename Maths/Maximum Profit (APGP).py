class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) # inventory high to low 
        inventory += [0]
        MOD = 10**9 + 7
        # print(inventory)
        res = 0 
        for i in range(len(inventory) - 1):
            currentInv = inventory[i]
            nextInv = inventory[i + 1]
            maximumAble = (currentInv - nextInv) * (i + 1) # width 
            # print(maximumAble, i, "maxi")
            if orders > maximumAble:
                orders -= maximumAble 
                oneStackOrder = currentInv - nextInv
                # use arithmetic here 
                oneStackOrderAmount = (currentInv)*(currentInv + 1)//2 - (currentInv - oneStackOrder) * (currentInv - oneStackOrder + 1) // 2
                # print(oneStackOrderAmount , "one stack")
                res += oneStackOrderAmount * (i + 1)
            else:
                # that means order <= maximumAble 
                oneStackOrder = orders // (i + 1) # so how many I can buy from each 
                orders -= oneStackOrder * (i + 1)
                oneStackOrderAmount = (currentInv)*(currentInv + 1)//2 - (currentInv - oneStackOrder) * (currentInv - oneStackOrder + 1) // 2
                
                res += oneStackOrderAmount*(i + 1)
                if orders > 0: # that means theres a 1 remainder, 
                    res += (currentInv - oneStackOrder) * orders
                
                
                return res % MOD