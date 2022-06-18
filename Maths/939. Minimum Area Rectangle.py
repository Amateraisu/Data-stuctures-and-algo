class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # first I need to store every y coordinate in a x 
        points.sort()
        hashtable = defaultdict(list)
        for x, y in points:
            hashtable[x].append(y)
            
        res = float("inf")
        visited = {}
        sortedTable = sorted(hashtable)
        
        for x in sortedTable:
            yList = hashtable[x]
            yList.sort()
            for index1 in range(len(yList)):
                y1 = yList[index1]
                for j in range(index1 + 1, len(yList)):
                    y2 = yList[j]
                    if (y1, y2) in visited:
                        area = (x - visited[(y1, y2)]) * (y2 - y1)
                        res = min(area, res)
                        
                    visited[(y1, y2)] = x 
        return res if res != float("inf") else 0