class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # compute the individual areas 
        
        area1 = getArea(ax1, ay1, ax2, ay2)
        area2 = getArea(bx1, by1, bx2, by2)
        
        doesOverlap, overlapArea = getOverlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        
        
        if doesOverlap:
            return area1 + area2 - overlapArea 
        
        
        return area1 + area2 
    
        
def getOverlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    
    overlappedArea = 0 
    doesOverlap = False
    

    # if one is enclosed in another 
    left = max(ax1, bx1)
    right = min(ax2, bx2)
    x_overlap = right - left

    # calculate y overlap
    top = min(ay2, by2)
    bottom = max(ay1, by1)
    y_overlap = top - bottom

    area_of_overlap = 0
    # if the rectangles overlap each other, then calculate
    # the area of the overlap
    if x_overlap > 0 and y_overlap > 0:
        area_of_overlap = x_overlap * y_overlap
        doesOverlap = True 

    # area_of_overlap is counted twice when in the summation of
    # area_of_a and area_of_b, so we need to subtract it from the
    # total, to get the toal area covered by both the rectangles


    return [doesOverlap, area_of_overlap]
    
    
    

    
        
        
        
def getArea(bottomLeftx, bottomLefty, upperRightx, upperRighty):
    
    height = abs(bottomLefty - upperRighty)
    width = abs(bottomLeftx - upperRightx)
    
    return height * width