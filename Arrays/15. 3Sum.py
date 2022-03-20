class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) ==1 or len(nums) == 0:
            return []
        
        res = []
   
        nums.sort()
        
        print(nums)
        for index, num in enumerate(nums):
            target = 0 - num
            
            ptr1 = index + 1
            ptr2 = len(nums)-1
            

            while ptr1 < ptr2:
                
                numberOne = nums[ptr1]
                numberTwo = nums[ptr2]
                
                
                total = numberOne + numberTwo

                
                if total < target:

                    ptr1 +=1 
                elif total > target:

                    ptr2 -=1
                    
                elif target == total:

                    res.append([num,numberOne,numberTwo])
                    ptr1 +=1
                    ptr2 -=1
        finalRes= []
        for answer in res:
            if answer not in finalRes:
                finalRes.append(answer)
            else:
                continue
                
        return finalRes