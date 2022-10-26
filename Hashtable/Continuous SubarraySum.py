
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        myDict = {}
        
        # print("test", 2%6)
        pref = [0] * len(nums)
        pref[0] = nums[0]
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] + nums[i]
        # print(pref)
        for j in range(len(nums)):
            currentPrefix = pref[j]
            if currentPrefix % k == 0 and j != 0:
                return True 
            
            remainder = currentPrefix % k 

            if remainder in myDict and j - myDict[remainder] >= 2 :

                return True 
            if remainder not in myDict:
                myDict[remainder] = j


        return False