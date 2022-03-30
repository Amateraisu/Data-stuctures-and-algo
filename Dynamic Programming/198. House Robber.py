class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) ==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        maxRob = [0 for x in range(len(nums))]
        maxRob[0] = nums[0]
        maxRob[1] = nums[1]
        print(maxRob)
        for robAmount in range(2,len(maxRob)):
            
            print(maxRob[0:robAmount-1])
            maxRob[robAmount] = max(maxRob[0:robAmount-1]) + nums[robAmount]
            
        return max(maxRob)