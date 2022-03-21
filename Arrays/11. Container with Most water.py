class Solution:
    def maxArea(self, height: List[int]) -> int:
        # so basically find the 2 largest numbers 
        # then take the lower number for the height
        #breadth use index and minus 
        # I think this is just another variant of 2 sum
        #so first obviously we can just use 2 for loops and brute force it 
        # then time complexity will be O(n^2) and space complexity will be O(1) 
        
        maxArea = 0 
        
        ptr1 = 0 
        ptr2 = len(height)-1
        
        while ptr1 < ptr2:
            height1 = height[ptr1]
            height2 = height[ptr2]
            width = ptr2 - ptr1
            
            currentArea = min(height1, height2) * width
            if currentArea > maxArea:
                maxArea = currentArea
            if height1 < height2:
                ptr1+=1
            else:
                ptr2-=1
            
            #decrement or increment the one that is lower in height 
        return maxArea