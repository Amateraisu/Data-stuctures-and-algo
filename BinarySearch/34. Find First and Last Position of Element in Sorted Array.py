class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findRight(target):
            left = 0 
            right = len(nums) - 1 
            res = None
            while left <= right:
                # print(left, right)
                mid = left + (right - left)//2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1 
                else:
                    right = mid - 1 
            return res

        def findLeft(target):
            left = 0 
            right = len(nums) - 1
            res = None
            while left <= right:
                mid = left + (right - left)//2 
                if nums[mid] == target:
                    res = mid 
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1 
                else:
                    right = mid - 1
            return res 


        left = findLeft(target)
        right = findRight(target)

        return [left, right] if left != None and right != None else [-1, -1]