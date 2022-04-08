class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        #reverse nums2 
        # this is nlogn time operation because of the sort
        # O(1) space complexity 
        ptr1 = 0 
        ptr2 = len(nums2)-1
        while ptr1 < ptr2 :
            nums2[ptr1] , nums2[ptr2] = nums2[ptr2], nums2[ptr1]
            ptr1 += 1
            ptr2 -=1
        
        ptr1 = 0
        total = 0
        while ptr1 < len(nums2):
            
            total += nums1[ptr1] * nums2[ptr1]
            ptr1+=1
            
        return total