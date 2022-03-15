class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can mutliply everything together, by looping through the array once first.
        #Time complexity of n+n, = O(2n) = O(n). Space complexity of O(1)
        
        #starting from index 1, 
        #ignore the zeros first
        totalProduct = 1
        containsZero = 0
        ans = []
        for num in nums:
            if num ==0 :
                containsZero += 1
                
            else:
                totalProduct *= num
        
        if containsZero>1:
            totalProductNoZero = totalProduct
            totalProduct = 0
            for num in nums:
                
                ans.append(0)
                
        elif containsZero == 1:
            totalProductNoZero = totalProduct
            totalProduct = 0
            for num in nums:
                if num == 0:
                    toAdd = totalProductNoZero
                    ans.append(int(toAdd))
                else:
                    ans.append(0)
        else:
            for num in nums:
                ans.append(int(totalProduct/num))
                
                
        return ans