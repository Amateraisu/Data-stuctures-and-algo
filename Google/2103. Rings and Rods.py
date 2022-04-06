class Solution:
    def countPoints(self, rings: str) -> int:
        #time complexity is O(n) time and O(n) space
        numberOfRings = len(rings)//2
        hashmap = {}

        
        for i in range(0,len(rings),2):
            ringNumber = rings[i+1]
            if ringNumber not in hashmap:
                hashmap[ringNumber] = [rings[i]]
            else:
                hashmap[ringNumber].append(rings[i])
            
        
        return numberOfRodWithAllThreeColours(hashmap)
    
def numberOfRodWithAllThreeColours(rings):
    count = 0
    for ring in rings:
        if 'R' in rings[ring] and 'G' in rings[ring] and 'B' in rings[ring]:
            count+=1
    return count