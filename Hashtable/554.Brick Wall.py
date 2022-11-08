class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        numRows = len(wall)

        counter = defaultdict(int)
        length = sum(wall[0])
        for row in range(numRows):
            current = 0 
            for col in range(len(wall[row])):
                currentLength = wall[row][col]
                current += currentLength 
                counter[current] += 1 
                
        
        counter.pop(length)

        if len(counter) == 0:
            return numRows

        
        
        return numRows - max(counter.values())