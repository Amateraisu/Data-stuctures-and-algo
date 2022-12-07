class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        coords = [p1, p2, p3, p4]
        test = (tuple(coord) for coord in coords)
        
        if len(set(test)) < 4:
            return False
        lengths = set()
        for coord1 in coords:
            for coord2 in coords:
                if coord1 == coord2:
                    continue
                length = dist(coord1, coord2)
                lengths.add(length)

        return len(lengths) == 2
        

    def dist(p1, p2):
        return (p1[0]-p2[0]) ** 2 + (p1[1] - p2[1]) ** 2