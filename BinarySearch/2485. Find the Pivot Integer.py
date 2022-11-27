class Solution:
    def pivotInteger(self, n: int) -> int:
        res = -1 
        summation = n * (n - 1) / 2
        
        left = 0 
        right = n
        while left <= right:
            mid = left + (right - left)//2 
            # print("middle", mid)
            leftCount = ((mid-1)/2) * (mid)
            rightCount = (n/2)*(1 + n) - (mid/2) * (1 + mid)
            
            # print(leftCount, rightCount, mid)
            if leftCount == rightCount:
                return mid 
            
            elif leftCount < rightCount:
                left = mid + 1 
            else:
                right = mid - 1 
            
            
        return -1 