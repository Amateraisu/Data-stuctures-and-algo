class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        queue = collections.deque()
        l = r = 0
        
        for i in range(len(nums)):
            r = i
            
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            
            
            if l > queue[0]:
                queue.popleft()
                
            if (r+1) >= k:
                output.append(nums[queue[0]])
                l+=1

        return output