class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        miniMaxArray = [[0,0] for num in nums]
        # so 0 will be the max , 1 will be the min
        
        
        #set base case here 
        miniMaxArray[0][0], miniMaxArray[0][1] = nums[0],nums[0]
        for numIndex in range(1, len(miniMaxArray)):
            miniMaxArray[numIndex][0] = max(nums[numIndex] , miniMaxArray[numIndex-1][1] * nums[numIndex], nums[numIndex] * miniMaxArray[numIndex-1][0])
            miniMaxArray[numIndex][1] = min(nums[numIndex] , miniMaxArray[numIndex-1][1] * nums[numIndex], nums[numIndex] * miniMaxArray[numIndex-1][0])
            
        finalArray = [num[0] for num in miniMaxArray]
        
        return max(finalArray)