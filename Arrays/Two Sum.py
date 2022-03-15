class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        
        for index,num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], index]
            else:
                hashmap[num] = index
        return []