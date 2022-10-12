class Solution:
    def solve(self, nums, k):
        # we want to split it into k chunks 
        # we want use binary search to find a range in which we can split them 
        # so we want to find a range in which we can split it into at least k chunks 


        # return the maximum possible value == we want to try and expand the range right ? 

        # so make it left = mid + 1 when my condition is fulfilled 

        # else : make it right = mid - 1 



        # so whats our condition? 
        # we want to split our nums array into k chunks 
        # so, initially it is min(nums), sum(nums)
        

        # then we check our middle 

        # mid = num (a target number which we want to maximize)

        # so, 
        # [1, 5], [3, 4], [7] 
        # if u see these cunks ,

        # 6, 7 , 7 

        # this is the biggest smallest sum 
        def canSplit(target):
            cursum = 0
            cnt = 0
            for p in nums:
                cursum += p
                if cursum >= target:
                    cnt += 1
                    cursum = 0
                    if cnt == k:
                        return True
            return False


                

        left = min(nums)
        right = sum(nums)

        res = 0 


        while left <= right:
            mid = left + (right - left)//2 


            if canSplit(mid):
                res = max(res, mid)
                left = mid + 1 
            else:
                right = mid - 1 

        return res 