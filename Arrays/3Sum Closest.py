


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # maybe I can do O()

        res = float("inf")
        diff = float("inf")
        # find the len(keys) relative to nums 
        # if len(keys) > nums:
        # then do the set 
        # this is O(n^2)
        nums.sort()
        for i in range(2, len(nums)):
            ptr1 = 0 
            ptr2 = i - 1 
            currentNumber = nums[i]
            # print(currentNumber + nums[ptr1] + nums[ptr2])
            while ptr1 < ptr2:
                currentTotal = currentNumber + nums[ptr1] + nums[ptr2]
                if currentTotal == target:
                    return target
                elif currentTotal > target:
                    ptr2 -= 1 
                else:
                    ptr1 += 1 
                currentDifference = abs(target - currentTotal)
                if currentDifference < diff:
                    diff = currentDifference 
                    res = currentTotal
                    
        return res 