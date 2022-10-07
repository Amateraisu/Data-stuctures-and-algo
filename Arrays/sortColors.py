class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numbers = [0] * 3
        for num in nums:
            numbers[num] += 1 

        res1 = numbers[0] * [0]
        res2= [1] * numbers[1]
        res3= [2] * numbers[2]

        res = res1 + res2 +res3 
        for index, num in enumerate(res):
            nums[index] = num
        return 