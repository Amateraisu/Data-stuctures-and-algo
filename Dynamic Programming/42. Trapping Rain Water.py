        # O(n) time complexity and O(n) space complexity 
#         maxLeft = [0 for level in height]
#         maxRight = [0 for level in height]
#         res = 0 
#         for i in range(1,len(maxLeft)):
#             maxLeft[i] = max(maxLeft[i-1], height[i-1])
            
#         for i in reversed(range(len(maxRight)-1)):
#             maxRight[i] = max(maxRight[i+1], height[i+1])
#         for index, level in enumerate(height):
#             maxLeftHeight = maxLeft[index]
#             maxRightHeight = maxRight[index]
#             currentHeight = height[index]
            
#             minimum = min(maxLeftHeight, maxRightHeight)
#             heightOfWater = minimum - currentHeight
#             if heightOfWater < 0:
#                 continue
#             else:
#                 res += heightOfWater
#         return res
        ptr1 = 0
        ptr2 = len(height)-1
        res = 0
        leftMax, rightMax = height[ptr1], height[ptr2]
        while ptr1 < ptr2:
            if leftMax < rightMax:
                ptr1 += 1
                leftMax = max(leftMax, height[ptr1])
                res += leftMax - height[ptr1]
            else:
                ptr2 -= 1
                rightMax = max(rightMax, height[ptr2])
                res += rightMax - height[ptr2]
                
        return res