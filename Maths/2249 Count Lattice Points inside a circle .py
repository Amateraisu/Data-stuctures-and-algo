class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for circle in circles:
            x,y,r = circle
            for i in range(x-r,x+r+1):
                for j in range(y-r,y+r+1):
                    radius = math.sqrt((i-x)**2 + (j-y)**2)
                    if radius <= r:

                        res.add((i,j))

        return len(res)