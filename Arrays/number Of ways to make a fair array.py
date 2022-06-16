class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # first find the total sum of even and odd indexes 
        # 2 1 6 4 
        # total = 13 
        # even = 8 ,   2, 6 
        # odd = 5 ,   1, 4 
        totalSum = 0 # 
        totalOdd = 0 # 5
        totalEven = 0 # 8
        
        for i in range(len(nums)):
            if i % 2 == 0:# this is even index
                totalEven += nums[i]
            else:
                totalOdd += nums[i]
            totalSum += nums[i]
            
        currentOddSum = 0 
        currentEvenSum = 0 

        res = 0 
            
        for j in range(len(nums)):

            if j % 2 ==0 :
                oddSum = totalEven - nums[j] - currentEvenSum + currentOddSum
                evenSum = totalOdd - currentOddSum + currentEvenSum
                
                currentEvenSum += nums[j]
            elif j % 2 != 0:
                evenSum = totalOdd - nums[j] - currentOddSum + currentEvenSum 
                oddSum = totalEven - currentEvenSum + currentOddSum 
                
                currentOddSum += nums[j]
                
            if evenSum == oddSum:
                res += 1 
        return res
            