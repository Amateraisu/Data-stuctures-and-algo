class Solution:
    def solve(self, nums, k):
        if k >= len(nums):
            return sum(nums)
        if k == 0:
            return 0 


        myDictionarySum = {}
        current = 0 
        # front 
        for index in range(k):
            num = nums[index]
            current += num 
            myDictionarySum[(index + 1, "left")] = current

        # reverse 
        current = 0
        for index in range(k):
            num = nums[len(nums) - index - 1]
            current += num 
            myDictionarySum[(index + 1, "right")] = current 
        myDictionarySum[(0, "left")] = 0 
        myDictionarySum[(0, "right")] = 0 
        # then try the different combinations 
        res = float("-inf")

        for left in range(0, k + 1):
            res = max(res, myDictionarySum[(left, "left")] + myDictionarySum[(k - left, "right")])
        # print(myDictionarySum)
        return res