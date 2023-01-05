class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # convex hull, 
        # graham scan 
        # find the lowest y coordinate 
        
        def orientation(a, b, c):
            # if it is +ve, it is to the left side, 
            # if it is negative, it is to the right side 
            
            AB = [b[0] - a[0], b[1] - a[1]]
            AC = [c[0] - a[0], c[1] - a[1]]
            # this is just a change in gradient  
            
            return AB[0] * AC[1] - AB[1] * AC[0]
        
        
        trees.sort()
        upper = []
        lower = []
        
        for t in trees:
            
            while len(upper) >= 2 and orientation(upper[-1],upper[-2],t)>0:
                upper.pop()
            
            while len(lower) >= 2 and orientation(lower[-1],lower[-2],t)<0:
                lower.pop()
            
            upper.append(tuple(t))
            lower.append(tuple(t))
        
        return list(set(upper+lower))